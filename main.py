from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain import question
from domain.answer import answer

app = FastAPI()


origins = [
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question.router)
app.include_router(answer.router)