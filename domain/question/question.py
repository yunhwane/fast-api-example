from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.question import question_crud, question_schema
from domain.question.question_schema import create_question

router = APIRouter(
    prefix="/api/v1/question"
)


@router.get("/lists", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list


@router.get("/{question_id}", response_model=question_schema.Question)
def question_item(item_id: int, db: Session = Depends(get_db)):
    question_by_id = question_crud.get_question_by_id(db, item_id)
    return question_by_id


@router.post("/create", status_code=status.HTTP_201_CREATED)
def question_create(_question_create: create_question, db: Session = Depends(get_db)):
    question_crud.create_question(db, _question_create)
