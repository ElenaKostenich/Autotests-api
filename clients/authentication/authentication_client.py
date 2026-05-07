from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

class LoginRequestDict(TypedDict):
    """
       Structure of authentication request
    """
    email: str
    password: str

class RefreshRequestDict(TypedDict):
    """
    Type for dictionary with refreshToken
    """
    refreshToken: str


class AuthenticationClient(APIClient):
    """
    Client for /api/v1/authentication endpoints
    """
    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Method performs user authentication
        :param request: dict with email and password
        :return:  server's response as a httpx.Response object
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Method performs user authentication token
        :param request: dict with refreshToken
        :return: server's response as a httpx.Response object
        """
        return self.post("/api/v1/authentication/refresh", json=request)