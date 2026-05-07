from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class UpdateUserRequestDict(TypedDict):
    """
    Structure of update user request
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class PrivateUsersClient(APIClient):
    """
    Client for private users /api/v1/users/ endpoints
    """
    def get_get_user_me_api(self) -> Response:
        """
        Get current user
        :return: Server response as a httpx.Response object
        """
        return self.get('/api/v1/users/me')

    def get_get_user_api(self, user_id: str) -> Response:
        """
        Get user by id
        :param user_id: User id
        :return: Server response as a httpx.Response object
        """
        return self.get(f'/api/v1/users/{user_id}')

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Update user by id
        :param user_id: User id
        :param request: Dict with email, lastName, firstName and middleName
        :return: Server response as a httpx.Response object
        """
        return self.patch(f'/api/v1/users/{user_id}', json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Delete user by id
        :param user_id: User id
        :return: Server response as a httpx.Response object
        """
        return self.delete(f'/api/v1/users/{user_id}')