from pydantic import BaseModel


class ResponseMessage(BaseModel):
    status: bool
    message: str
