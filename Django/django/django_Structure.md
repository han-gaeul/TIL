### `Django`

***

#### 🔎 프로젝트 구조

- `collection of apps`
  - 프로젝트는 앱의 집합
  - 프로젝트에는 여러 앱이 포함될 수 있음
- `__init__.py`
  - Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
  - 별도로 추가 코드를 작성하지 않음
- `asgi.py`
  - Asynchronous Server Gateway Interface
  - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
  - 추후 배포 시에 사용하며 지금은 수정하지 않음
- `settings.py`
  - Django 프로젝트 설정을 관리
- `urls.py`
  - 사이트의 url과 적절한 views의 연결을 지정
- `wsgi.py`
  - Web Server Gateway Interface
  - Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
  - 추후 배포 시에 사용하며 지금은 수정하지 않음
- `manage.py`
  - Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

<hr>

#### 🔎 애플리케이션 구조

- 앱은 여러 프로젝트에 있을 수 있음
- 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할을 담당
- 일반적으로 앱은 하나의 역할 및 기능 단위로 작성하는 것을 권장
- `admin.py`
  - 관리자용 페이지를 설정하는 곳
- `apps.py`
  - 앱의 정보가 작성된 곳
  - 별도로 추가 코드를 작성하지 않음
- `models.py`
  - 애플리케이션에서 사용하는 Model을 정의하는 곳
  - MTV 패턴의 M에 해당
- `tests.py`
  - 프로젝트의 테스트 코드를 작성하는 곳
- `views.py`
  - view 함수들이 정의 되는 곳
  - MTV 패턴의 V에 해당
- `INSTALLED_APPS`
  - Django installation에 활성화 된 모든 앱을 지정하는 문자열 목록
  - 프로젝트에서 앱을 사용하기 위해서는 반드시 `INSTALLED_APPS` 리스트에 추가해야 함