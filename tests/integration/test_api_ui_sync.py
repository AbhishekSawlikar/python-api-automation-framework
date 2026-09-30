import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Integration Suite")
@allure.feature("API to Frontend Sync")
class TestApiUiSync:

    @pytest.fixture(scope="function")
    def driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=chrome_options)
        yield driver
        driver.quit()

    @allure.story("Verify API User Exists and Displays Correctly in UI")
    @pytest.mark.integration
    def test_verify_user_in_frontend(self, api_client, driver):
        user_id = 1

        with allure.step("Fetch target user data from Backend API"):
            api_res = api_client.get(f"/users/{user_id}")
            assert api_res.status_code == 200
            api_user = api_res.json()
            expected_name = api_user["name"]

        with allure.step("Open Frontend Application and Verify User Renders"):
            # Mock UI inspection using JSONPlaceholder's live interactive endpoint UI
            driver.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")

            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "pre")))

            page_text = element.text
            assert expected_name in page_text, \
                f"Sync Failure: UI missing user name {expected_name}"