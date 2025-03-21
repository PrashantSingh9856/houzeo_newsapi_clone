from pydantic import BaseModel
from typing import Optional
from app.schemas.source import Source
from datetime import datetime


class Article(BaseModel):
    source: Source
    author: Optional[str]
    title: str
    description: Optional[str]
    url: str
    urlToImage: Optional[str]
    publishedAt: datetime
    content: Optional[str]
