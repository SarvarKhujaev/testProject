import typing
from rest_framework import status
import rest_framework.exceptions as exception
from django.http.response import JsonResponse

"""
обрабатывает ошибки и исключения
также хранит метод для работы с Response
"""


class ErrorInspector:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance

    @typing.final
    def raise_error(self, error: exception.APIException = exception.ValidationError, message: str = ""):
        raise error

    @typing.final
    def get_response(
            self,
            message: str,
            api_status: status = status.HTTP_204_NO_CONTENT) -> JsonResponse:
        return JsonResponse(
            data={
                'message': message,
            }, status=api_status,
        )
