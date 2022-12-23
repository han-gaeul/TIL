### `Django - Sending and Retrieving form data`

***

#### 📚 Sending and Retrieving form data

- 데이터를 보내고 가져오기
- HTML form element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기

- `Client & Server architecture`
  - 웹은 다음과 같이 가장 기본적으로 클라이언트-서버 아키텍처를 사용
    - 클라이언트*(일반적으로 웹 브라우저)*가 서버에 요청을 보내고 서버는 클라이언트의 요청에 응답
  - 클라이언트 측에서 HTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법
  - 이를 통해 사용자는 HTTP 요청에서 전달할 정보를 제공할 수 있음

***

#### 📚 Sending form data (Client)

- `HTML <form> element`

  - 데이터가 전송되는 방법을 정의
  - 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit 등)을 제공하고 **사용자로부터 할당된 데이터를 서버로 전송**하는 역할을 담당
  - "데이터를 어디(`action`)로 어떤 방식(`method`)으로 보낼지"
  - 핵심 속성
    - `action`
    - `method`

- `HTML form's attributes`

  - `action`
    - 입력 데이터가 전송될 URL을 지정
    - 데이터를 어디로 보낼 것인지 지정하는 것이며 이 값은 반드시 유효한 URL이어야 함
    - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
  - `method`
    - 데이터를 어떻게 보낼 것인지 정의
    - 입력 데이터의 HTTP request methods를 지정
    - HTML form 데이터는 오직 2가지 방법으로만 전송 할 수 있는데 `GET` 방식과 `POST` 방식

  ```html
  <!-- templates/index.html -->
  
  {% extends 'base.html'}
  
  {% block content %}
  <h1>index</h1>
  <form action="#" method="#"></form>
  {% endblock %}
  ```

- `HTML <input> element`

  - 사용자로부터 데이터를 입력 받기 위해 사용
  - `type` 속성에 따라 동작 방식이 달라짐
    - `input` 요소의 동작 방식은 `type` 특성에 따라 현격히 달라짐
    - `type`을 지정하지 않은 경우 기본값은 `text`
  - 핵심 속성
    - `name`

  ```html
  <!-- templates/index.html -->
  
  {% extends 'base.html'}
  
  {% block content %}
  	<h1>index</h1>
  	<form action="#" method="#">
      <label for="message">index</label>
  		<input type="text" id="message" name="message">
  		<input type="submit">
  	</form>
  {% endblock %}
  ```

  

- `HTML input's attribute`

  - `name`

    - `form`을 통해 데이터를 제출(`submit`)했을 때 `name` 속성에 설정된 값을 서버로 전송하고 서버는 `name` 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있음
    - 주요 용도는 `GET`/`POST` 방식으로 서버에 전달하는 파라미터(`name`은 `key`, `value`는 `value`)로 매핑하는 것
      - `GET` 방식에서는 URL 형식으로 데이터를 전달

    ```url
    '?key=value&key=value/'
    ```

- `HTTP request methods`

  - `HTTP`

    - HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
    - 웹에서 이루어지는 모든 데이터 교환의 기초
    - 주어진 리소스가 수행할 원하는 작업을 나타내는 request methods를 정의
    - 자원에 대한 행위*(수행하고자 하는 동작)*를 정의
    - 주어진 리소스*(자원)*에 수행하길 원하는 행동을 나타냄
    - HTTP Method 예시
      - GET, POST, PUT, DELETE
    - `GET`
      - `GET`과 `get` 모두 대소문자 관계없이 동일하게 동작하지만 명시적 표현을 위해 대문자 사용을 권장
      - 데이터를 입력 후 submit 버튼을 누르고 URL의 변화를 확인

    ```html
    <!-- index.html -->
    
    {% extends 'base.html'}
    
    {% block content %}
    	<h1>index</h1>
    	<form action="#" method="GET">
        <label for="message">index</label>
    		<input type="text" id="message" name="message">
    		<input type="submit">
    	</form>
    {% endblock %}
    ```

- `Query String Parameters`

  - 사용자가 입력 데이터를 전달하는 방법 중 하나
  - url 주소에 데이터를 파라미터를 통해 넘기는 것
  - 문자열은 앰퍼샌드(`&`)로 연결된 `key=value` 쌍으로 구성되며 기본 URL과 물음표(`?`)로 구분됨
  - Query String이라고도 함
  - 정해진 주소 이후에 물음표를 쓰는 것으로 Query String이 시작함을 알림
  - `key=value`로 필요한 파라미터의 값을 적음
    - `=`로 key와 value가 구분됨
  - 파라미터가 여러 개일 경우 `&`를 붙여 여러 개의 파라미터를 넘길 수 있음

***

#### 📚 Retrieving the date (Server)

- 데이터 가져오기(검색하기)

  - 모든 요청 데이터는 `view` 함수의 첫번째 인자 `request`에 들어있음

- 서버는 클라이언트로 받은 key-value 쌍의 목록과 같은 데이터를 받게 됨

- 이러한 목록에 접근하는 방법은 사용하는 특정 프레임워크에 따라 다름

- `action 작성`

  - `index` 페이지에서 `form`의 `action` 부분을 마저 작성하고 데이터를 보냄

  ```html
  <!-- index.html -->
  
  {% extends 'base.html'}
  
  {% block content %}
  	<h1>index</h1>
  	<form action="/detail/" method="GET">
      <label for="message">index</label>
  		<input type="text" id="message" name="message">
  		<input type="submit">
  	</form>
  {% endblock %}
  ```

  - `detail 작성`

  ```python
  def detail(request):
    message = request.GET.get('message')
    context = {
      'message' : message,
    }
    return render(reuqest, 'detail.html', context)
  ```

  ```html
  <!-- templates/detail.html -->
  
  {% extends 'base.html'}
  
  {% block content %}
  	<h1>detail</h1>
  	<p>여기서 {{ message }}를 받았음</p>
  {% endblock %}
  ```

- `Request and Response objects`

  - 요청과 응답 객체 흐름
    1. 페이지가 요청되면 Django는 요청에 대한 메타데이터를 포함하는 HttpRequest object를 생성
    2. 그리고 해당하는 적절한 view 함수를 로드하고 HttpRequest를 첫번째 인자로 전달
    3. 마지막으로 view 함수는 HttpResponse object를 반환

***

#### 📚 Django URLs

- Dispatcher로서의 URL 이해하기
- 웹 어플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작함
- URL 끝에 `/(Trailing slash)`가 없다면 자동으로 붙여주는 것이 기본 설정
  - 모든 주소가 `/`로 끝나도록 구성되어 있음
  - 하지만 모든 프레임워크가 이렇게 동작하는 것은 아님