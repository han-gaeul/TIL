### `Django templates/view`

***

#### 🗒 Variable routing

- URL 주소를 변수로 사용하는 것을 의미

- URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음

- 즉, 변수 값에 따라 하나의 `path()`에 여러 페이지를 연결 시킬 수 있음

- `작성`

  - 변수는 `<>`에 정의하며 view 함수의 인자로 할당됨
  - 기본 타입은 `string`이며 5가지 타입으로 명시할 수 있음
  - `str`
    - `/`를 제외하고 비어 있지 않은 모든 문자열
    - 작성하지 않을 경우 기본 값
  - `int`
    - 0 또는 양의 정수와 매치

- View 함수 작성

  - variable routing으로 할당된 변수를 인자로 받고 템플릿 변수로 사용할 수 있음

  ```python
  # app/views.py
  
  def index(request, name):
    context = {
      'name' : name,
    }
    return render(request, 'index.html', context)
  ```

  ```html
  <!-- app/templates/index.html -->
  
  {% extends 'base.html' %}
  {% block content %}
  	<p>반갑습니다, {{ name }}님</p>
  {% endblock %}
  ```

***

#### 🗒 Template

- `Django Template`

  - 데이터 표현을 제어하는 도구이자 표현에 관련된 로직

  - Template을 이용한 HTML 정적 부분과 동적 컨텐츠 삽입

  - Template System의 기본 목표를 숙지
    - 데이터 표현을 제어하는 도구이자 표현에 관련된 로직을 담당

- `Django Template Language(DTL)`

  - template에서 사용하는 built-in template system
  - 조건, 반복, 변수 치환, 필터 등의 기능을 제공
    - python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 python 코드로 실행되는 것은 아님
    - 단순히 python이 HTML에 포함된 것이 아니니 주의
  - 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것임을 명심

- `DTL Syntax`

  - `Variable`

    ```html
    {{ variable }}
    ```

    - 변수명은 영어, 숫자와 밑줄(`_`)의 조합으로 구성될 수 있으나 밑줄로는 시작할 수 없음
      - 공백이나 구두점 문자 또한 사용 불가
    - `dot(.)`을 사용하여 변수 속성에 접근할 수 있음
    - `render()`의 세번째 인자로 `{'key': value}`와 같이 딕셔너리 형태로 넘겨주며 여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
    - 실습

    ```python
    # views.py
    
    def greeting(request):
      foods = ['apple', 'banana', 'peach']
      info = {
        'name' : 'gildong'
      }
      context = {
        'foods' : foods,
        'info' : info,
      }
      return render(request, 'greeting.html', context)
    ```

    ```html
    <!-- templates/greeting.html -->
    
    <p>안녕하세요, 저는 {{ info.name }}입니다.</p>
    <p>저는 {{ foods.2 }}를 가장 좋아합니다.</p>
    ```

  - `Filters`

    ```html
    {{ variable|filter }}
    ```

    - 표시할 변수를 수정할 때 사용
    - 예
      - name 변수를 모두 소문자로 출력

    ```html
    {{ name|lower }}
    ```

    - 60개의 built-in template filters를 제공
    - chained가 가능하며 일부 필터는 인자를 받기도 함

    ```html
    {{ name|turncatewords:30 }}
    ```

    - 실습

    ```python
    # urls.py
    
    urlpatterns = [
      path('dinner/', views.dinner),
    ]
    ```

    ```python
    # views.py
    
    import random
    from django.shortcuts import render
    
    def dinner(request):
      foods = ['피자', '햄버거', '치킨']
      pick = random.choice(foods)
      context = {
        'pick' : pick,
        'foods' : foods,
      }
      return render(request, 'dinner.html', context)
    ```

    ```html
    <!-- templates/dinner.html -->
    
    <p>{{ pick }}은 {{ pick|length }}글자</p>
    <p>{{ foods|join", " }}</p>
    ```

  - `Tags`

    ```html
    {% tag %}
    ```

    - 출력 텍스트를 만들거나 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
    - 일부 태그는 시작과 종료 태그가 필요

    ```html
    {% if %} {% endif %}
    ```

    - 약 24개의 built-in template tags를 제공

    - 실습

    ```html
    <!-- templates/dinner.html -->
    
    <p>{{ pick }}은 {{ pick|length }}글자</p>
    <p>{{ foods|join", " }}</p>
    
    <p>메뉴판</p>
    <ul>
      {% for food in foods %}
        <li>{{ food }}</li>
      {% endfor %}
    </ul>
    ```

  - `Comments`

    ```html
    {# #}
    ```

    - template에서 라인의 주석을 표현하기 위해 사용
    - 한 줄 주석에만 사용할 수 있음 (줄 바꿈 허용 X)
    - 여러 줄 주석은 `{% comment %}`와 `{% endcomment %}` 사이에 입력

***

#### 🗒 Template inheritance

- `템플릿 상속`

  - 기본적으로 코드의 재사용성에 초점을 맞춤
  - 상속을 사용하면 사이트의 모든 공통 요소를 포함하고 하위 템플릿이 재정의(override) 할 수 있는 블록을 정의하는 기본 `skeleton` 템플릿을 만들 수 있음

- `관련 태그`

  - `{% extends '' %}`

    - 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림

    - <span style='background-color: #f5f0ff'>반드시 템플릿 최상단에 작성 되어야 함*(즉, 2개 이상 사용할 수 없음)*</span>

    - 하위 템플릿에서 재지정(overriden)할 수 있는 블록을 정의

    - 즉, 하위 템플릿이 채울 수 있는 공간

    - 가독성을 높이기 위해 선택적으로 `endblock` 태그에 이름을 지정할 수 있음

    - 예시

      - `base`라는 이름의 `skeleton` 템플릿을 작성

      ```html
      <!-- templates/base.html -->
      
      <!DOCTYPE html>
      <html lang="en">
      <head>
      	<meta charset="UTF-8">
      	<meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- bootstrap CDN 작성 -->
      	<title>Document</title>
      </head>
      <body>
      	{% block content %}
      	{% endblock content %}
      	<!-- bootstrap CDN 작성 -->
      </body>
      </html>
      ```

      - `index` 템플릿에서 `base` 템플릿을 상속 받음

      ```html
      <!-- index.html -->
      
      {% extends 'base.html' %}
      
      {% block content %}
      <h1>안녕하세요.</h1>
      {% endblock content %}
      ```

    - 추가 템플릿 경로 추가하기
    
      - 기본 `template` 경로가 아닌 다른 경로를 추가하기 위해 다음 코드를 작성
    
      ```python
      # setting.py
      
      TEMPLATES = [
        {
          ...
          'DIRS' : [
            BASE_DIR / 'templates',
          ],
          ...
        }
      ]
      ```
      
      - `app_name/templates/` 디렉토리 경로 외 추가 경로를 설정한 것
      - `base.html`의 위치를 다음과 같이 이동 후 상속에 문제가 없는지 확인

