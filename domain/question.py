from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain import question_schema, question_crud
from models import Question

router = APIRouter(
    prefix="/question"
)


@router.get("/lists", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list


@router.get("/{item_id}", response_model=question_schema.Question)
def question_item(item_id: int, db: Session = Depends(get_db)):
    question_by_id = question_crud.get_question_by_id(db,item_id)
    return question_by_id
