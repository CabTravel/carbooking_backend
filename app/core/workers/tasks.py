from app.core.workers.celery_app import celery_app
import time
from app.core.workers.schemas.otp_generate_worker_param import GenerateOtpParam

from app.core.services.sms_service import messageService


@celery_app.task(
    name="send_otp",
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={
        "max_retries":5
    }
)
def send_otp(self,data: dict):

    print("generate otp process started")

    phone_number = data["phoneNumber"]
    otp = data["otp"]

    messageService.send_otp(
        phone_number=phone_number,
        otp=otp
    )

    return {
        "status": "Success",
        "phoneNumber": phone_number
    }

    

@celery_app.task(
    name="calculation_task",
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={
        "max_retries":5
    }
)
def calculation_task(
    user_id: str,
):

    print(f"Starting calculation for {user_id}")

    result = 0

    for i in range(10_000_000):
        result += i

    print("Calculation completed")

    return {
        "user_id": user_id,
        "result": result,
    }