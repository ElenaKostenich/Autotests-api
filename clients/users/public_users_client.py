from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient

class CreateUserRequestDict(TypedDict):
    """
    Structure of create user request
    """
    email: str
    password: str
    firstName: str
    lastName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Client for public /api/v1/users/ endpoints
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Creates a new user.

        :param request: dict with email, password, firstName, lastName and middleName
        :return:  server response as a httpx.Response object
        """
        return self.post("/api/v1/users", json=request)