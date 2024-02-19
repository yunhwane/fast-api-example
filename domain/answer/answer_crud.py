from datetime import datetime

from sqlalchemy.orm import Session

from domain.answer.answer_schema import AnswerCreate
from models import Question, Answer


def create_answer(db: Session, question: Question, answer_create: AnswerCreate):
    db_answer = Answer(content = answer_create.content, create_date=datetime.now(), Question = question )
    db.add(db_answer)
    db.commit()

