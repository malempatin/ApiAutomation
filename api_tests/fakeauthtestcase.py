from http.client import responses

import requests
import json
import utils.api_utils as utilTest

BaseUrl = "https://reqres.in/"

def fake_token():
    response = utilTest.api_call(BaseUrl,"/api/users", "GET", "hskjdhsiudhiuehie")
    assert response.status_code == 401
def missing_required_fields():
    user_data = {"job" : "qe engineer"}
    response = utilTest.api_call(BaseUrl,"/api/users", "POST", user_data)
    assert response["name"]
def invalid_endpoint():
    utilTest.api_call(BaseUrl, "api/use", "GET")

