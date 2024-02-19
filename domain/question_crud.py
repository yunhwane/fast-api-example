import datetime

from sqlalchemy.orm import Session

from domain.question_schema import create_question
from models import Question


def get_question_list(db: Session):
    question_list = db.query(Question) \
        .order_by(Question.create_date.desc()) \
        .all()
    return question_list


def get_question_by_id(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question

def create_question(db: Session, _create_question: create_question):
    db_question = Question(subject=_create_question.subject, content=_create_question.content, create_date=datetime.datetime.now())
    db.add(db_question)
    db.commit()
