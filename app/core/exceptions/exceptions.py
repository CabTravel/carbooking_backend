from fastapi import HTTPException,status
from collections.abc import Mapping


class AppException(Exception):
    def __init__(self, message:str,status_code:int=500):
        self.message=message
        self.status_code=status_code

        super().__init__(message)

    
        


def raise_exception(
    details: str = "couldn't validate credentials",statusCode: int = 401, header: Mapping[str, str] | None = None,)-> HTTPException:
    return HTTPException(
        detail=details,
        status_code=statusCode,
        headers=header

    )