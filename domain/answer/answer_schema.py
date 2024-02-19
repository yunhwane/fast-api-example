from pydantic import BaseModel
from pydantic.v1 import validator


class AnswerCreate(BaseModel):
    content: str

    @validator('content')
    def not_empty_content(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


