### `Django - Namespace`

***

#### 🔎 URL namespace

- URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에는 이름이 지정된 URL을 고유하게 사용할 수 있음

- **app_name** attribute를 작성해 URL namespace를 설정

  ```python
  # app1/urls.py
  
  app_name = 'app1'
  urlpatterns = [
    ...,
  ]
  
  # app2/urls.py
  
  app_name = 'app2'
  urlpatterns = [
    ...,
  ]
  ```

- URL tag의 변화

  ```html
  {% url 'index' %} ➡︎ {% url 'app1:index' %}
  ```

- <span style='background-color: #f5f0ff'>`app_name`을 지정한 이후에는 url 태그에서 반드시 `app_name:url_name` 형태로만 사용해야 함. 그렇지 않으면 `NoReverceMatch` 에러 발생</span>

- URL 참조
  - `:` 연산자를 사용하여 지정
  - 예) `app_name`이 `app1`이고 `URL name`이 `index`인 주소 참조는 `app1:index`가 됨

***

#### 🔎 Template namespace

- Django는 기본적으로 **app_name/templates/** 경로에 있는 templates 파일들만 찾을 수 있으며 `settings.py`의 `INSTALLED_APPS`에 작성한 app 순서로 template을 검색 후 렌더링 함

  ```python
  # PJT/setting.py
  
  TEMPLATES = [
    {
      ...,
      'APP_DIRS' : True,
      ...,
    },
  ]
  ```

- 디렉토리 생성을 통해 물리적인 이름공간 구분

  - Django templates의 기본 경로에 app과 같은 이름의 폴더를 생성해 폴더 구조를 **app_name/templates/app_name/** 형태로 변경
  - Django templates의 기본 경로 자체를 변경할 수는 없기 때문에 물리적으로 이름 공간을 만드는 것

  ```
  app1/
  	templates/
  		app1/
  			index.html
  			
  app2/
  	templates/
  		app2/
  			index.html
  ```

- 템플릿 경로 변경

  - 폴더 구조 변경 후 변경된 경로로 해당하는 모든 부분을 수정하기

  ```python
  # app1/views.py
  
  return render(request, 'app1/index.html')
  
  # app2/views.py
  
  return render(request, 'app2/index.html')
  ```

- 반드시 사용해야 할까?

  - 단일 앱으로만 이루어진 프로젝트라면 상관 없음
  - 여러 앱이 되었을 때에도 템플릿 파일 이름일 겹치지 않으면 되지만 앱이 많아지면 대부분은 같은 이름의 템플릿 파일이 존재하게 됨

***

#### 🔎 Naming URL patterns

- Naming URL patterns의 필요성

  - 링크에 URL을 직접 작성하는 것이 아니라 `path()` 함수의 `name` 인자를 정의해서 사용
  - DTL의 Tag 중 하나인 **URL 태그**를 사용해서 `path*` 함수에 작성한 `name`을 사용할 수 있음
  - 이를 통해 URL 설정에 정의된 특정한 경로들의 의존성을 제거할 수 있음
  - Django는 URL에 이름을 지정하는 방법을 제공함으로써 view 함수와 템플릿에서 특정 주소를 쉽게 참조할 수 있게 도움

- Built-in tag-'url'

  ```
  {% url '' %}
  ```

  - 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환
  - 템플릿에 URL을 하드 코딩하지 않고도 DRY 원칙을 위반하지 않으면서 링크를 출력하는 방법

  

  