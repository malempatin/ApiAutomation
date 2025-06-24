from jsonschema import validate

import json
import requests

BaseUrl = "https://reqres.in/"

def test_get_users():
    response = requests.get(f"{BaseUrl}/api/users")
    print(response.status_code)
    assert response.status_code == 200
    user_data = response.json()
    assert "data" in user_data
    assert len(user_data["data"]) > 0
    #print(user_data["data"])
    detailed_user_data = user_data["data"][0]
    print("detailed_user_data:", detailed_user_data)
    get_user_first_name = detailed_user_data["first_name"]
    print("get_user_first_name", get_user_first_name)

    detailed_user_data.get("first_name")
    print("detailed_user_data:", detailed_user_data)

def test_create_user():
    payload = {"name" : "paravthi", "email": "mamepf@gsde.com"}
    response = requests.post(f"{BaseUrl}/api/users",  json=payload)
    print(response.status_code)
    assert response.status_code == 201
    get_response = requests.get(f"{BaseUrl}/api/users")
    response_json =  get_response.json()
    print(response_json)
    assert response.status_code == 200

def test_update_user():
    response = requests.get(f"{BaseUrl}/api/users/2")
    user_details = response.json()
    print(user_details)
    user_name = user_details["data"]["first_name"]
    print("user_name:", user_name)
    user_details["data"]["first_name"] = user_name
    user_details["data"]["last_name"] = "test"
    put_response = requests.put(f"{BaseUrl}/api/users/2", json=user_details)
    print(put_response.status_code)
    print(put_response.text)

def test_delete_user():
    response = requests.delete(f"{BaseUrl}/api/users/2")
    assert response.status_code == 204
    print("user is deleted")
    assert requests.get(f"{BaseUrl}/api/users/2").status_code == 404



user_schema_temp = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "email": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "avatar": {"type": "string"}
            },
            "required": ["id", "email", "first_name"]
        }
    },
    "required": ["data"]
}

def load_schema(fileName):
    with open(fileName) as json_file:
        return json.load(json_file)

def test_user_schema():
    response = requests.get(f"{BaseUrl}/api/users/2")
    data= response.json()
    user_schema = load_schema("utils/user_schema.json")
    print(data)
    validate(data, user_schema)


