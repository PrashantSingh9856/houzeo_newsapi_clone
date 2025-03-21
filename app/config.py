from dotenv import load_dotenv

load_dotenv()
import os

DATABASE_ENGINE = os.getenv("DATABASE_ENGINE", "mysql+mysqlconnector")
DATABASE_USER = os.getenv("DATABASE_USER", "news_user")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "securepassword")
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_NAME = os.getenv("DATABASE_NAME", "news_db")
DATABASE_PORT = os.getenv("DATABASE_PORT", "3306")
DATABASE_URL = f"{DATABASE_ENGINE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

NEWS_API_URL = os.getenv("NEWS_API_URL", "")
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "")
