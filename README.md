
# * Domain
* 라우터 파일 - URL과 API의 전체적인 동작을 관리
* 데이터베이스 처리 파일 - 데이터의 생성(**C**reate), 조회(**R**ead), 수정(**U**pdate), 삭제(**D**elete)를 처리 (CRUD)
* 입출력 관리 파일 - 입력 데이터와 출력 데이터의 스펙 정의 및 검증


예를 들어 질문(domain/question) 도메인이라면 다음의 3개 파일이 필요하다.
* question_router.py - 라우터 파일
* question_crud.py - 데이터베이스 처리 파일
* question_schema.py - 입출력 관리 파일



## ALEMBIC 
- FestAPI 테이블 자동 생성 및 버전 관리 

```pip install alembic```

- 초기화 
```
alembic init migrations
```

- alembic.ini 수정
```
sqlalchemy.url = “db 정보”
```

- /migrations/env.py
```
import models

target_metadata = models.Base.metadata
```

- revision 파일 생성
```
alembic revision --autogenerate
```

- revision 파일 실행
```
alembic upgrade head
```


## 데이터베이스 자동화 
```
@contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

```

- 반복되는 db 트랜잭션 자동화 
- @Transactional 역할

제너레이터 함수에 @contextlib.contextmanager 어노테이션을 적용했으므로 다음과 같이 with 문과 함께 사용

변경된 코드 
```
@router.get("/lists")
def question_list():
    with get_db() as db:
        _questions = db.query(Question).order_by(Question.create_date.desc()).all()
    return _questions

```

Depends를 사용한 간단 코드 
```@router.get("/list")
def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list
```

get_db 함수를 with문과 함께 쓰는 대신에 question_list 에 주입받았음
* [https://fastapi.tiangolo.com/tutorial/dependencies/](https://fastapi.tiangolo.com/tutorial/dependencies/)


## Pydantic

- FastAPI 입출력 spec 정의하고, 그 값을 검증하기 위한 라이브러리 

Pydantic - [https://pydantic-docs.helpmanual.io/](https://pydantic-docs.helpmanual.io/)

- 항목, 타입을 설정할 수 있음
- 필수값 체크 가능
- 데이터 검증 가능 

```
@router.get("/lists", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list

```

Pedantic 적용 모델 
```class Question(BaseModel):
    id: int
    subject: str | None = None
    content: str
    create_date: datetime

```

