import pytest
import allure
from jsonschema import validate
from payloads.user_payloads import UserPayloads
from schemas.user_schema import USER_RESPONSE_SCHEMA


@allure.epic("JSONPlaceholder Platform")
@allure.feature("User CRUD Service")
class TestCreateUser:

    @allure.story("Create User - Valid Payload & Schema Validation")
    @pytest.mark.crud
    @pytest.mark.smoke
    def test_create_user_success(self, api_client, cleanup_user):
        payload = UserPayloads.create_user_payload()

        with allure.step("Send POST /users request"):
            response = api_client.post("/users", json=payload)

        with allure.step("Validate 201 Created Status"):
            assert response.status_code == 201, f"Expected 201, received {response.status_code}"

        data = response.json()
        cleanup_user(data.get("id"))

        with allure.step("Verify Response Fields"):
            assert data["name"] == payload["name"]
            assert data["email"] == payload["email"]
            assert "id" in data

        with allure.step("Validate JSON Schema"):
            validate(instance=data, schema=USER_RESPONSE_SCHEMA)

    @allure.story("Create User - Parameterized Data Ingestion")
    @pytest.mark.parametrize("custom_name, custom_email", [
        ("Alice Cooper", "alice@example.com"),
        ("Bob Marley", "bob@example.com")
    ])
    def test_create_user_parameterized(self, api_client, custom_name, custom_email):
        payload = UserPayloads.create_user_payload(name=custom_name, email=custom_email)
        response = api_client.post("/users", json=payload)
        assert response.status_code == 201
        assert response.json()["name"] == custom_name
        assert response.json()["email"] == custom_email