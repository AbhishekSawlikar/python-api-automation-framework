import allure
import pytest
from payloads.user_payloads import UserPayloads

@allure.epic("JSONPlaceholder Platform")
@allure.feature("End-to-End User Lifecycle")
class TestUserE2E:

    @allure.story("Full Cycle: POST -> GET -> PUT -> PATCH -> DELETE")
    @pytest.mark.crud
    def test_complete_user_lifecycle(self, api_client):
        # 1. CREATE
        with allure.step("Step 1: CREATE user via POST"):
            init_payload = UserPayloads.create_user_payload()
            create_res = api_client.post("/users", json=init_payload)
            assert create_res.status_code == 201
            # JSONPlaceholder returns id=11 for created objects
            user_id = 1

        # 2. READ
        with allure.step("Step 2: READ user details via GET"):
            get_res = api_client.get(f"/users/{user_id}")
            assert get_res.status_code == 200
            assert "email" in get_res.json()

        # 3. UPDATE (PUT)
        with allure.step("Step 3: FULL UPDATE user via PUT"):
            updated_payload = UserPayloads.create_user_payload(name="Fully Updated Name")
            put_res = api_client.put(f"/users/{user_id}", json=updated_payload)
            assert put_res.status_code == 200
            assert put_res.json()["name"] == "Fully Updated Name"

        # 4. PARTIAL UPDATE (PATCH)
        with allure.step("Step 4: PARTIAL UPDATE user email via PATCH"):
            patch_payload = {"email": "patch.updated@example.com"}
            patch_res = api_client.patch(f"/users/{user_id}", json=patch_payload)
            assert patch_res.status_code == 200
            assert patch_res.json()["email"] == "patch.updated@example.com"

        # 5. DELETE
        with allure.step("Step 5: DELETE user"):
            del_res = api_client.delete(f"/users/{user_id}")
            assert del_res.status_code == 200