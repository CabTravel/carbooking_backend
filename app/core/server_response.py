
from typing import Generic, TypeVar
from pydantic import BaseModel
from fastapi import HTTPException,status


T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    statusCode: int=200
    message: str='Success'
    data: T


class FailureResponse(BaseModel):
    statusCode: int
    message: str='operation failed'


def failureFromException(exception:HTTPException) -> FailureResponse:
    return FailureResponse(
        statusCode=exception.status_code,
        message=exception.detail
    )


