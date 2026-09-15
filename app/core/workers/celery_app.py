from celery import Celery


celery_app = Celery(
    "backend",
    broker="amqp://guest:guest@rabbitmq:5672//",
    backend="redis://redis:6379/1",
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",

    timezone="Asia/Kolkata",
    enable_utc=True,

    task_track_started=True,
    imports = (
        "app.core.workers.tasks"
    ),

    task_acks_late=True,

    worker_prefetch_multiplier=1,
    task_routes= {
        "send_otp":{
            "queue":"otp_queue"
        },
        "calculation_task":{
            "queue":"calculation_queue",
        }
    }
)