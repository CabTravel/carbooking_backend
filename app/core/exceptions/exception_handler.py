from fastapi import Request,HTTPException
from fastapi.responses import JSONResponse
from app.core.exceptions.exceptions import AppException

async def global_exception_handler(
        request:Request,
        exc:Exception
            ):
    return JSONResponse(
        status_code=500,
        content={
            'status_code':500,
            'message':"Internal server error"
        }
    )

async def http_exception_handler(
        request:Request,
        exc:HTTPException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            'statusCode':exc.status_code,
            'message':str(exc.detail)
        }
    )

async def app_exception_handler(request:Request,exc:AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            'statusCode':exc.status_code,
            'message':exc.message
        }

    )
    