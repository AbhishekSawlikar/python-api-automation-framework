import pytest
from config.config import Config
from helpers.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    return APIClient(base_url=Config.BASE_URL, timeout=Config.TIMEOUT)