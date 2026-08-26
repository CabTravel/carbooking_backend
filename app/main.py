from fastapi import FastAPI,HTTPException
from app.core.exceptions.exception_handler import global_exception_handler,http_exception_handler,app_exception_handler

from app.core.exceptions.exceptions import AppException

from app.modules.authentication.router import router as AuthRouter
from app.modules.bookings.router import router as BookingsRouter
from  app.modules.car.router import router as CarRouter
from app.modules.expenses.router import router as ExpenseRouter
from app.modules.file.router import router as FileRouter
from app.core.server_response import SuccessResponse



app=FastAPI()

app.add_exception_handler(AppException,app_exception_handler)

app.add_exception_handler(
    HTTPException,
    http_exception_handler

)
app.add_exception_handler(
    Exception,
    global_exception_handler
)

app.include_router(AuthRouter)
app.include_router(BookingsRouter)
app.include_router(CarRouter)
app.include_router(ExpenseRouter)
app.include_router(FileRouter)

@app.get('/health')
def health():
    return {
        'statusCode':200,
        'message':'Health check okay',
        'health':'ok'
    }

@app.get('/')
def root():
    return {
        'message':'Server running okay'
    }
@app.get('/check')
def checking():
    return SuccessResponse(data="dinesh")


