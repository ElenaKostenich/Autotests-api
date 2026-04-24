import httpx

login_payload = {
  "email": "user@example.com",
  "password": "string"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_json = login_response.json()
access_token = login_response_json["token"]["accessToken"]

print("Login json :", login_response_json)
print("Login status code: ", login_response.status_code)
print("accessToken", access_token)

headers = {"Authorization": f"Bearer {access_token}"}
user_me_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=headers)
print(user_me_response.status_code)
print(user_me_response.json())