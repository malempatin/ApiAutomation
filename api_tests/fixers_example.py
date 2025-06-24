import utils.api_utils as api_utils
import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/"

@pytest.fixture
def test_user_payload():
    return {
        "name": "Alex",
        "job": "SDET"
    }

@pytest.fixture
def fake_token():
    return "fake-token-123"

def test_create_user(base_url, test_user_payload):
    response = api_utils.api_call(base_url, "api/users", "POST", input_json=test_user_payload)
    print(response.json())
    assert response.status_code == 201
    assert response.json()["name"] == test_user_payload["name"]

