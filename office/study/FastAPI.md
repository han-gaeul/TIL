### FastAPI

\#FastAPI란?

- API를 만들기 위한 파이썬 웹 framework

\#기존 framework와의 차이점

- API를 만드는데 보다 집중한 framework

- FastAPI로 작성한 API는 Vue.js와 같은 Frontend 웹 framework에서 사용할 수 있고 모바일 앱에서도 사용할 수 있음. 즉, 한 번 만든 API를 여러 클라이언트에서 변경 없이 사용할 수 있음

    > 만약 Django나 Flask로 웹 서비스를 만들었다면 이에 대응하는 모바일 앱을 위한 API 개발을 따로 해야 함 Django나 Flask로 API를 만들지 못하는 것은 아니지만 FastAPI가 좀 더 유리함 Django에는 FastAPI와 비슷한 역할을 하는 DRF(Django REST Framework)가 있음

\#장점

- 빠른 속도

    - NodeJS 및 Go와 대등할 정도로 높은 성능
    - 내부적으로 Starlette라는 비동기 framework를 사용하기 때문에 가능

- 빠른 작성

    - 입출력을 정의하고 입출력 값의 검증을 빠르고 안전하게 할 수 있음

        > Pydantic을 사용해 가능

    - 작성한 API는 자동으로 생성되는 API 문서(웹 문서)를 통해 손쉽게 테스트

        > Swagger를 사용해 가능

\#데이터베이스

- Django처럼 자체 ORM을 제공하지 않지만 SQLAlchemy를 사용해 ORM을 사용할 수 있음

------

### FastAPI 프로젝트 생성하기

\#가상 환경 및 프로젝트 디렉터리 생성하기

```bash
# 가상 환경 디렉터리 생성
C:\\> mkdir venv
C:\\> cd venv
C:\\venv> python -m venv venv

# 프로젝트 디렉터리 생성
C:\\> mkdir projects
C:\\> cd projects

# 가상 환경 진입
C:\\projects> C:\\venv\\venv\\Scripts\\activate
(venv) C:\\projects
```

\#API 만들기

```python
# projects/venv/main.py

from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def hello():
		return {'message': '안녕하세요'}
```

- 설명

    FastAPI 클래스로 생성한 app객체가 FastAPI의 핵심 개체. 모든 동작은 이 객체로부터 비롯됨

    함수명 위에 `app.get('/hello')` 어노테이션은 `hello` 라는 URL 요청이 발생하면 해당 함수를 실행하여 결과는 리턴하라는 의미

    따라서, `/hello` 라는 URL이 요청되면 FastAPI는 `{'message': '안녕하세요'}` 라는 딕셔너리를 리턴할 것

```bash
# uvicorn 설치
(venv) C:/projects/venv pip install "uvicorn[standard]"

# 서버 실행
(venv) C:/projects/venv uvicorn main:app --reload
```

- 설명

    유비콘(uvicorn)은 비동기 호출을 지원하는 파이썬용 웹 서버

    `map:app` 에서 main은 [main.py](http://main.py) 파일을 의미하고 app은 main.py의 app 객체를 의미

    `--reload` 옵션은 프로그램이 변경되면 서버 재시작 없이 그 내용을 반영하라는 의미