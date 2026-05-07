from httpcore import Request
from httpx import Client, URL, QueryParams, Response
from typing import Any

from httpx._types import RequestData, RequestFiles


class APIClient:
    def __init__(self, client: Client):
        """
        Base API client that accepts an httpx.Client instance.

        :param client: an instance of httpx.Client used to perform HTTP requests
        """
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Performs a GET request.

        :param url: endpoint URL
        :param params: query parameters (e.g., ?key=value)
        :return: Response object containing server response data
        """
        return self.client.get(url, params=params)

    def post(
            self,
            url: URL | str,
            json: Any | None= None,
            data: RequestData | None = None,
            files: RequestFiles | None = None,
    ) -> Response:
        """
        Performs a POST request.

        :param url: endpoint URL
        :param json: data in JSON format
        :param data: form data (application/x-www-form-urlencoded)
        :param files: files to upload
        :return: Response object
        """
        return self.client.post(url, json=json, data=data, files=files)

    def patch(
            self,
            url: URL | str,
            json: Any | None = None
    ) -> Response:
        """
        Performs a PATCH request (partial update).

        :param url: endpoint URL
        :param json: data in JSON format
        :return: Response object
        """
        return self.client.patch(url, json=json)

    def delete(self, url: URL | str) -> Response:
        """
        Performs a DELETE request.
        :param url: endpoint URL
        :return: Response object
        """
        return self.client.delete(url)
