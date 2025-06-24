import pytest
import requests

BaseUrl = "https://reqres.in/"

@pytest.mark.parametrize("page", [1, 2, 3])
def test_get_users_param(page):
    response = requests.get(f"{BaseUrl}/api/users", params={"page": page})
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)