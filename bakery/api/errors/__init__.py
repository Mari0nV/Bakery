from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder


class ApiException(HTTPException):
    def __init__(self, status_code: int, error: dict):
        super().__init__(
            status_code, jsonable_encoder({"error": type(self).__name__, **error})
        )
