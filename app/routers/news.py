import logging
from typing import Optional
from newsapi import NewsApiClient
from app.config import NEWS_API_KEY
from app.database.connection import get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel, ValidationError
from app.schemas.response import ResponseMessage
from fastapi import APIRouter, Depends, Query, HTTPException
from app.schemas.top_headlines_response import TopHeadlinesResponse
from app.database.operation_handler import DatabaseOperationHandler

newsapi = NewsApiClient(api_key=NEWS_API_KEY)

router = APIRouter(
    prefix="/v1/news",
    tags=["news"],
)


class TopHeadlinesQuery(BaseModel):
    q: Optional[str] = Query(None, description="Search term")
    language: Optional[str] = Query(None, description="Language code (e.g., 'en')")
    country: Optional[str] = Query(None, description="Country code (e.g., 'us')")
    sources: Optional[str] = Query(None, description="Comma-separated source list")


@router.get("/top-headlines", response_model=ResponseMessage)
def get_top_headlines(
    params: TopHeadlinesQuery = Depends(), db: Session = Depends(get_db)
):
    """Fetch top headlines with query parameters."""
    logging.info("Fetching top headlines with parameters: %s", params)
    query_params = params.model_dump(exclude_none=True)
    top_headlines = newsapi.get_top_headlines(**query_params)
    if top_headlines.get("status") != "ok":
        logging.error("Failed to fetch top headlines.")
        raise HTTPException(status_code=400, detail="Failed to fetch top headlines.")
    try:
        logging.info("Successfully fetched top headlines.")
        top_headlines = TopHeadlinesResponse(**top_headlines)
        return DatabaseOperationHandler(db).save_article(top_headlines.articles)
    except ValidationError as e:
        logging.error("Invalid response format: %s", e.errors())
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Invalid response format",
                "validation_errors": e.errors(),
            },
        )
