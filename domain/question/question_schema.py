from datetime import datetime
from typing import List

from pydantic import BaseModel

from domain.answer.answer_schema import Answer


class Question(BaseModel):
    id: int
    subject: str | None = None
    content: str
    create_date: datetime
    answers: List[Answer] = []


class create_question(BaseModel):
    subject : str
    content : str