from pydantic import BaseModel
from typing import Optional


class Source(BaseModel):
    id: Optional[str]
    name: str
