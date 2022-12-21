#### 가상환경 생성/실행

- `.gitignore`로 가상환경 폴더가 Git에 관리되지 않게 설정

- `생성`

  ```zsh
  python3 -m venv [가상환경 이름]
  ```

  > 가상환경의 이름은 대부분 `venv`를 사용함

- `실행`

  ```zsh
  source [가상환경 이름]/bin/activate
  
  . [가상환경 이름]/bin/activate
  ```

  

#### Django LTS 버전 설치

- `LTS란?`

  - `Long-term support(LTS) releases	`
  - 장기지원 되는 버전

- `설치`

  ```zsh
  pip install django==[설치할 버전]
  ```

  > 나는 3.2.13 버전을 설치

  - `확인`

  ```zsh
  pip list
  ```

- `패키지 관리`

  - `pip`로 여러 패키지를 설치하게 되는데 매번 설치하기 번거로움
  - `requirements.txt`
    - 패키지 목록이 나열된 텍스트 파일
    - 생성

  ```zsh
  pip freeze > requirements.txt
  ```

  > 대부분의 PJT에서 `requirements.txt`라는 이름으로 관리함

  - 패키지 설치

  ```zsh
  pip install -r requorements.txt
  ```

  > 텍스트 파일 나열된 목록들의 패키지가 한 번에 설치 됨
  >
  > 
  >
  > *(참고)* `Django==3.2.13` 같은 경우 `Django`라는 패키지를 3.2.13 버전으로 설치한다는 뜻
  >
  > 단순히 해당 버전 이상을 설치하고 싶다면 `Django>=3.2.13`라고 변경
  >
  > 만약 3 버전대의 아무 버전이나 설치하고 싶다면 `Django>=3.`라고 변경



#### Django PJT/App 생성

- `생성`

  ```zsh
  django-admin startproject [PJT 이름] [경로]
  ```

  - 경로 입력은 선택사항
    - `.` 명령어로 현재 디렉터리 안에 PJT 생성
    - 경로를 입력하지 않으면 `PJT 이름`으로 된 디렉터리 안에 또 `PJT 이름`으로 된 프로젝트가 생성됨

- `실행`

  ```zsh
  python3 manage.py runserver
  ```

  > 서버 실행 전 현재 경로에 `manage.py` 파일이 있는지 확인

  - `확인`
    - 브라우저 주소창에 `localhost:8000` 입력
    - 로켓 이미지가 나오면 잘 실행된 것

- `App 생성`

  ```zsh
  python3 manege.py startapp [App 이름]
  ```

  

#### PJT/App 설정

- `App 등록`

  ```python
  # PJT/settings.py -> INSTALLED_APPS
  
  INSTALLED_APPS ={
    '[App name]',
  }
  ```

  ```python
  # PJT/urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('[App name].urls')),
  ]
  ```

  ```python
  # App/urls.py
  
  from django.urls import path
  from . import views
  
  app_name = '[App name]'
  
  urlpatterns = [
    path('', views.index, name='index'),
  ]
  ```

  > `작은 따옴표 ''` 안에 아무것도 입력 하지 않으면 `root page`로 생성됨
  >
  > 서버 실행 후 브라우저 주소창에 `localhost:8000`만 입력해도 자동으로 `index` 페이지로 연결됨

- `.html 생성`

  ```python
  # 최상단 디렉터리/templates/base.html
  
  ...
    <body>
      {% block content %}
      {% endblock %}
    </body>
  ...
  ```

  ```python
  # App/templates/articles/index.html
  
  {% extends 'base.html' %}
  
  {% block content %}
  {% endblock %}
  ```

- `함수 생성`

  ```python
  # App/views.py
  
  from django.shortcuts import render
  
  def index(request):
    return render(reqeust, 'articles/index.html')
  ```

  

class Review(models.Model):

​    title = models.CharField(max_length=50)

​    content = models.TextField()

​    movie_name = models.CharField(max_length=50)

​    grade = models.IntegerChoices()

​    created_at = models.DateTimeField(auto_now_add=True)

​    updated_at = models.DateTimeField(auto_now=True)