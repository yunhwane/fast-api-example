

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.answer import answer_schema, answer_crud
from domain.question_crud import get_question_by_id
from models import Question

router = APIRouter(
    prefix="/api/v1/answer"
)

@router.post("/create/{question_id}", status_code=status.HTTP_201_CREATED)
def answer_create(question_id: int, _answer_create: answer_schema.AnswerCreate, db: Session = Depends(get_db)):
    question = get_question_by_id(db, question_id)
    if not question: raise HTTPException(status_code = 404, detail = "등록한 질문이 없습니다.")
    answer_crud.create_answer(db, question, _answer_create)



