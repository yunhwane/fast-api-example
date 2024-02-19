from datetime import datetime

from pydantic import BaseModel


class Question(BaseModel):
    id: int
    subject: str | None = None
    content: str
    create_date: datetime


class create_question(BaseModel):
    subject : str
    content : str