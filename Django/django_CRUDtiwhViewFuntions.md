### `Django - CRUD with view funtions`

***

#### 📍 사전 준비

- bootstrap CDN 및 템플릿 추가 경로 작성

  ```html
  <!-- templates/base.html -->
  <!DOCTYPE html>
  <html lang="en">
  <head>
  	<meta charset="UTF-8">
  	<meta http-equiv="X-UA-Compatible" content="IE=edge">
  	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- bootstrap CSS CDN -->
  	<title>Document</title>
  </head>
  <body>
  	<div class="container"> {% block content %}
  	{% endblock content %}
  	</div>
    <!-- bootstrap JS CDN -->
  </body>
  </html>
  ```

  ```python
  # PJT/settings.py
  
  TEMPLATES = [
    {
      ...,
      'DIRS' : [
        BASE_DIR / 'templates',
      ],
      ...,
    },
  ]
  ```

- url 분리 및 연결

  ```python
  # PJT/urls.py
  
  form django.contrib import admin
  from djnago.urls import path, include
  
  urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),
  ]
  ```

  ```python
  # app1/urls.py
  
  from django.urls import path
  from . import views
  
  app_name = 'app1'
  
  urlpatterns = [
    path('', views.index, name='index'),
  ]
  ```

  ```python
  # app1/views.py
  
  def index(request):
    return render(request, 'app1/index.html')
  ```

  ```html
  <!-- templates/app1/index.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  	<h1>index</h1>
  {% endblock content %}
  ```

***

#### 📃 READ 1 (index page)

- 전체 게시글 조회

  - index 페이지에서는 전체 게시글을 조회해서 출력

  ```python
  # app1/views.py
  
  from .models improt App1
  
  def index(request):
    app1 = App1.objects.all()
    context = {
      'app1' : app1,
    }
    return render(request, 'app1/index.html', context)
  ```

  ```html
  <!-- templates/app1/index.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  	<h1>index</h1>
  	<hr>
  	{% for app in app1 %}
  		<p>번호 : {{ app.pk }}</p>
  		<p>제목 : {{ app.title }}</p>
  		<p>내용 : {{ app.content }}</p>
  		<hr>
  	{% endfor %}
  {% endblock content %}
  ```

***

#### 📃 CREATE

- CREATE 로직을 구현하기 위해 view 함수 생성

  ```python
  # app1/urls.py
  
  urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
  ]
  ```

  ```python
  # app1/views.py
  
  def new(request):
    return render(reuqest, 'app1/new.html')
  ```

  ```html
  <!-- templates/app1/new.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  	<h1>new</h1>
  	<form action="#" method="GET">
      <label for="title">title : </label>
      <input type="text" name="title"><br>
      <label for="content">content : </label>
      <textarea name="content"></textarea><br>
      <input type="submit">
  	</form>
  	<br>
  	<a href="{% url 'app1:index' %}">back</a>
  {% endblock content %}
  ```

- new 페이지로 이동할 수 있는 하이펑 링크 작성

  ```html
  <!-- templates/app1/index.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  	<h1>index</h1>
  	<a href="{% url 'app1:new' %}">new</a>
  	<hr>
  	...
  {% endblock content %}
  ```

- create

  ```python
  # app1/urls.py
  
  utlpatterns = [
    ...,
    path('create/', views.create, name='create'),
  ]
  ```

  ```python
  # app1/views.py
  
  def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    app1 = App1(title=title, content=content)
    app1.save()
    return render(request, 'app1/create.html')
  ```

  - 게시글 작성 후 확인

  ```html
  <!-- templates/app1/create.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  	<h1>글 작성 완료</h1>
  {% endblock content %}
  ```

  ```html
  <!-- templates/app1/new.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  	<h1>new</h1>
  	<form action="{% url 'app1:create' %}" method="GET">
      <label for="title">title : </label>
      <input type="text" name="title"><br>
      <label for="content">content : </label>
      <textarea name="content"></textarea><br>
      <input type="submit">
  	</form>
  	<br>
  	<a href="{% url 'app1:index' %}">back</a>
  {% endblock content %}
  ```

  - 게시글 작성 후 index 페이지로 돌아가게 함

  ```python
  # app1/views.py
  
  def create(request):
    ...
    return render(request, 'app1/index.html')
  ```

  - Django shortcut function = `redirect()`

    - 인자에 작성된 곳으로 요청을 보냄

    - 사용 가능한 인자

      1. view name (URL pattern name)

         >return redirect('app1:index')

      2. absoute or relative URL

         > return redirect('/app1/')

    - 불필요해진 `create.html`는 삭제

  ```python
  # app1/views.py
  
  from django.shortcuts import render, redirect
  
  def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    app1 = App1(title=title, content=content)
    app1.save()
    # return render(request, '/app1/')
    return redirect('app1:index')
  ```

  - redirect 동작 원리

    - 클라이언트가 `create url`로 요청을 보냄

    - `create view` 함수에 `redirect` 함수가 `302 status code`를 응답

      > 302 Dound
      >
      > 해당 상태 코드를 응답 받으면 브라우저는 사용자를 해당 URL의 페이지로 이동시킴

    - 응답 받은 브라우저는 `redirect` 인자에 담긴 주소(`index`)로 사용자를 이동시키기 위해 `index url`로 Django에 재요청

    - `index page`를 정상적으로 응답 받음(`200 status code`)

- HTTP request method

  - `GET`
    - 특정 리소스를 가져오도록 요청할 때 사용
    - 반드시 데이터를 가져올 때만 사용해야 함
    - DB에 변화를 주지 않음
    - CRUD에서 R 역할을 담당
  - `POST`
    - 서버로 데이터를 전송할 때 사용
    - 서버에 변경사항을 반듦
    - 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송
    - GET의 쿼리 스트링 파라미터와 다르게 URL로 데이터를 보내지 않음
    - CRUD에서 C/U/D 역할을 담당
  - 정리
    - GET은 단순히 조회하려는 경우, POST는 서버나 DB에 변경을 요청하는 경우

- CSRF

  - Cross-Site-Request-Forgery
  - 사이트 간 요청 위조
  - 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
  - csrf_token 템플릿 태그
    - `{% csrf_token %}`
    - 해당 태그가 없다면 Django 서버는 요청에 대해 `403 forbidden`으로 응답
    - 템플릿에서 내부 URL로 향하는 Post form을 사용하는 경우 사용
    - `input type`이 hidden으로 작성되며 value는 Django에서 생성한 hash 값으로 설정
    - csrf_token은 해당 POST 요청이 내가 보낸 것인지를 검증하는 것

***

#### 📃 READ 2 (detail page)

- urls

  - URL로 특정 게시글을 조회할 수 있는 번호를 받음

  ```python
  # app1/urls.py
  
  urlpatterns = [
    ...,
    path('<int:pk>/', views.detail, name='detail'),
  ]
  ```

- views

  - `App1.objects.get(pk=pk)`에서 오른쪽 pk는 variable routing을 통해 받은 pk, 왼쪽 pksms DB에 저장된 레코드의 id 컬럼

  ```python
  # app1/views.py
  
  def detail(request):
    app1 = App1.objects.get(pk=pk)
    context = {
      'app1' : app1,
    }
    return render(request, 'app1/detail.html', context)
  ```

- templates

  ```html
  <!-- templates/app1/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  	<h1>detail</h1>
  	<h4>{{ app.pk }}번째 글</h4>
  	<hr>
  	<p>제목 : {{ app.title }}</p>
  	<p>내용 : {{ app.content }}</p>
  	<p>작성 시각 : {{ app.created_at }}</p>
  	<p>수정 시각 : {{ app.updated_at }}</p>
  	<hr>
  	<a href="{% url 'app1:index' %}">back</a>
  {% endblock content %}
  ```

  ```html
  <!-- templates/app1/index.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  	<h1>index</h1>
  	<a href="{% url 'app1:new' %}">new</a>
  	<hr>
  	{% for app in app1 %}
  		<p>번호 : {{ app.pk }}</p>
  		<p>제목 : {{ app.title }}</p>
  		<p>내용 : {{ app.content }}</p>
  		<a href="{% url 'app1:detail' app.pk %}">detail</a>
  		<hr>
  	{% endfor %}
  {% endblock content %}
  ```

- redirect 인자 변경

  ```python
  # app1/views.py
  
  def create(request):
    ...
    return redirect('app1:detail', app.pk)
  ```

***

#### 📃 DELETE

- urls

  - 모든 글을 삭제하는 것이 아니라 삭제하고자 하는 특정 글을 조회 후 삭제

  ```python
  # app1/urls.py
  
  urlpatterns = [
    ...,
    path('<int:pk>/delete/', views.delete, name='delete'),
  ]
  ```

- views

  ```python
  # app1/views.py
  
  def delete(requeset):
    app1 = App1.objects.get(pk=pk).delete()
    return redirect('app1:index')
  ```

- templates

  - detail 페이지에 작성하며 DB에 영향을 미치기 때문에 POST method 사용

  ```html
  <!-- app1/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  	<h1>detail</h1>
  	...
  	<form action="{% url 'app1:delete' app.pk %}" method="POST">
    	{% csrf_token %}
      <input type="submit" value="DELETE">
  	</form>
  	<a href="{% url 'app1:index' %}">back</a>
  {% endblock content %}
  ```

  