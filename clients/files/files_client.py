from clients.api_client import APIClient

from httpx import Response
from typing import TypedDict

class CreateFileRequestDict(TypedDict):
    """
    Structure for create file request
    """
    filename: str
    directory: str
    upload_file: str

class FilesClient(APIClient) :
    """
    Client for files /api/v1/files endpoint
    """
    def get_file_api(self, file_id: str) -> Response:
        """
        Get file method
        :param file_id:  File_id
        :return: Response as a httpx.Response object
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Create file method
        :param request: Dict with filename, directory, upload_file
        :return: Response as a httpx.Response object
        """
        return self.post(
            f"/api/v1/files",
            data=request,
            files={"upload_file": open(request["upload_file"], "rb")},
        )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Delete file method
        :param file_id: File_id
        :return: Response as a httpx.Response object
        """
        return self.delete(f"/api/v1/files/{file_id}")
