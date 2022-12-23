### `Dajngo - App URL mapping`

***

#### ✍️ App URL mapping

- 앱이 많아졌을 때 `urls.py`를 각 app에 매핑하는 방법을 이해하기
- 두번째 app인 `pages`를 생성 및 등록하고 진행
- app의 view 함수가 많아지면서 사용하는 `path()` 또한 많아지고 app 또한 더 많이 작성되기 때문에 프로젝트의 `urls.py`에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음

- 하나의 프로젝트에 여러 앱이 존재한다면 각각의 앱 안에 `urls.py`을 만들고 프로젝트 `urls.py`에서 각 앱의 `urls.py` 파일로 URL 매핑을 위탁할 수 있음

- **각각의 app 폴더 안에 `urls.py`를 작성**하고 다음과 같이 수정 진행

  ```python
  # app1/urls.py
  
  from django.urls import path
  from . import views
  
  urlpatterns = [
    path('index/', views.index)
    path('greeting/', views.greeting),
    path('dinner/', views.dinner),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<str:name>/', views.hello),
  ]
  ```

  ```python
  # app2/urls.py
  
  from django.urls import path
  
  urlpatterns = [
    
  ]
  ```

- `urlpattern`은 언제든지 다른 URLconf 모듈을 포함(`include`) 할 수 있음

- <span style='background-color: #f5f0ff'>`include` 되는 앱의 `urlst.py`에 `urlpatterns`가 작성되어 있지 않다면 에러가 발생함.</span>

  <span style='background-color: #f5f0ff'>예를 들어, `app2` 앱의 `urlpatterns`가 빈 리스트라도 작성되어 있어야 함</span>

  ```python
  # PJT/urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),
    path('app2/', include('app2.urls')),
  ]
  ```

- `include()`

  - 다른 URLconf(`app1/urls.py`)들을 참조할 수 있게 돕는 함수
  - 함수 `include()`를 만나게 되면 URL의 그 시점까지 일치하는 부분을 잘라내고 남은 문자열 부분을 후속 처리를 위해 `include`된 URLconf로 전달
  - URL 구조의 변화
    - 앱의 URL을 PJT의 `urls.py`에서 관리
    - 여러 개의 앱의 URL을 PJT의 `urls.py`에서 관리
    - 각각의 앱에서 URL을 관리

