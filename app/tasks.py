import logging
from celery import shared_task
from newsapi import NewsApiClient
from app.config import NEWS_API_KEY
from pydantic import ValidationError
from app.database.connection import get_db
from app.schemas.top_headlines_response import TopHeadlinesResponse
from app.database.operation_handler import DatabaseOperationHandler

newsapi = NewsApiClient(api_key=NEWS_API_KEY)


def save_articles(article_data):
    """Function to save articles to the database."""
    db = next(get_db())
    try:
        handler = DatabaseOperationHandler(db)
        return handler.save_article(article_data)
    finally:
        db.close()


@shared_task
def fetch_top_headlines(query_params=None, country="us"):
    logging.info("Fetching top headlines...")
    top_headlines = newsapi.get_top_headlines(
        q=query_params, language="en", country=country
    )
    if top_headlines.get("status") != "ok":
        logging.error("Failed to fetch top headlines.")
        return {"error": "Failed to fetch top headlines."}

    try:
        top_headlines = TopHeadlinesResponse(**top_headlines)
    except ValidationError as e:
        logging.error("Invalid response format: %s", e.errors())
        return {
            "error": "Invalid response format",
            "validation_errors": e.errors(),
        }

    return save_articles(top_headlines.articles).model_dump_json()


def delete_data():
    db = next(get_db())
    try:
        handler = DatabaseOperationHandler(db)

        return handler.delete_data()
    finally:
        db.close()
