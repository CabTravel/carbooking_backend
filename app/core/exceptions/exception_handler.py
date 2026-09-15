from fastapi import Request,HTTPException
from fastapi.responses import JSONResponse
from app.core.exceptions.exceptions import AppException

async def global_exception_handler(
        request:Request,
        exc:Exception
            ):
    print(f"in glocal exception handlerr ${str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            'status_code':500,
            'message':f"{str(exc.detail)} Internal server error"
        }
    )

async def http_exception_handler(
        request:Request,
        exc:HTTPException
):
    print(f"httpexception ${str(exc.detail)}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            'statusCode':exc.status_code,
            'message':str(exc.detail)
        }
    )

async def app_exception_handler(request:Request,exc:AppException):
    print(f" in app exception handler ${str(exc.message)}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            'statusCode':exc.status_code,
            'message':exc.message
        }

    )
    