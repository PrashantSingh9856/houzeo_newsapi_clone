from celery.app import Celery
from celery.schedules import crontab
from app.config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

celery_app = Celery(
    __name__,
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
    include=["app.tasks"],
)

celery_app.conf.update(
    timezone="Asia/Kolkata",
    enable_utc=True,
    task_serializer="json",
    broker_connection_retry_on_startup=True,
)


celery_app.conf.beat_schedule = {
    "run_every_1_minutes": {
        "task": "app.tasks.fetch_top_headlines",
        "schedule": crontab(minute="*/1"),  # Every 1 minutes
        "kwargs": {"query_params": None, "country": "us"},
    },
}
