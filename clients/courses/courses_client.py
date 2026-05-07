from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient

class GetCoursesQueryDict(TypedDict):
    """
    Structure of get the list of courses
    """
    userID: str

class CreateCourseRequestDict(TypedDict):
    """
    Structure of create course request
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCourseRequestDict(TypedDict):
    """
    Structure of update course request
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class CoursesClient(APIClient):
    """
    Client for Courses /api/v1/courses/
    """
    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Method to get the list of courses
        :param query: Dictionary with userID
        :return:  Response as a httpx.Response object
        """
        return self.get(f'/api/v1/courses/', params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Method to get course        :param course_id:  ID
        :return: Response as a httpx.Response object
        """
        return self.get(f'/api/v1/courses/{course_id}/')

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Method to create course
        :param request: Dictionary with title, maxScore, minScore, description,
        estimatedTime, previewFileId and createdByUserId
        :return: Response as a httpx.Response object
        """
        return self.post(f'/api/v1/courses/', json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Method to update course
        :param course_id:  courseID
        :param request: Dictionary with title, maxScore, minScore, description, estimatedTime
        :return: Response as a httpx.Response object
        """
        return self.patch(f'/api/v1/courses/{course_id}/', json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Method to delete course
        :param course_id:  courseID
        :return: Response as a httpx.Response object
        """
        return self.delete(f'/api/v1/courses/{course_id}/')