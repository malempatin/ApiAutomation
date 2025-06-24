import pytest
import pytest_html
print("pytest-html plugin is working")

@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/"

def test_user_payload():
    return {
        "name": "Alex",
        "job": "SDET"
    }

@pytest.fixture
def fake_token():
    return "fake-token-123"