import httpx

user_data_payload = {
    "email": "ivan@test.com",
    "password": "qwerty12345",
    "firstName": "Ivan",
    "lastName": "Ivanov",
    "middleName": "Ivanovich"
}

# response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=user_data_payload)
# user_data = response.json()
#
# print(user_data)
# print(response.status_code)

login_payload = {
    "email": "ivan@test.com",
    "password": "qwerty12345",
}
login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_json = login_response.json()
access_token = login_response_json["token"]["accessToken"]
print("Login response: ", login_response_json)
print("Login status code: ", login_response.status_code)

print(access_token)
headers = {"Authorization": f"Bearer {access_token}" }
user_me_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=headers)
print("User's status code: ", user_me_response.status_code)
print("User's response: ", user_me_response.json())