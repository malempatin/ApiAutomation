import requests


def api_call(url, endpoint, method, token=None, input_json=None):
    path = f"{url} + {endpoint}"
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    if method == "GET":
        response  = requests.get(path, headers=headers)
        return response.json()
    elif method == "POST":
        response = requests.post(path,input_json,  headers=headers)
        assert response.status_code == 201
        return response.json()
    elif method == "PUT":
        response = requests.put(path,input_json, headers=headers)
        assert response.status_code == 200
        return response.json()
    elif method == "DELETE":
        response = requests.delete(path, headers=headers)
        assert response.status_code == 204
    return None