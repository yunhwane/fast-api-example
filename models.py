from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship

from database import Base


class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    subject = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    create_date = Column(DateTime, nullable=False)


class Answer(Base):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey('question.id'))
    Question = relationship("Question", backref="answers")

#  역참조 relationship -> 한 질문에는 여러개의 답변인데, 역참조를 통해 질문에 달린 답변들을 참조할 수 있게 됨
# 테이블 잗동생성 alembic
# 1. pip install alembic
# 2. alembic init migrations
