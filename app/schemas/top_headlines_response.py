from pydantic import BaseModel
from typing import Optional
from typing import List
from app.schemas.articles import Article


class TopHeadlinesResponse(BaseModel):
    status: str
    totalResults: int
    articles: List[Article]
