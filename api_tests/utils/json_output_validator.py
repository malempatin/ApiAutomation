import json
from http.client import responses

import pytest
import requests
from jsonschema import ValidationError, validate

BaseUrl = "https://reqres.in/"

def load_json(filename):
    with open(filename) as json_file:
        return json.load(json_file)

def test_json_validator():
    try:
        response = requests.get(f"{BaseUrl}api/v1/users/1")
        validate(response.json, load_json("api_automation_swagger/api_tests/utils/user_schema.json"))

    except ValidationError as ve:
        print(ve.message)
        pytest.fail(ve.message)

test_json_validator()