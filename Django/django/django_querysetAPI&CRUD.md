### `Django - QuerySet API / CRUD`

***

#### 📍 사전 준비

- 추가 라이브러리 설치 및 설정

  ```zsh
  pip install ipython
  pip install django-extensions
  ```

  ```python
  # PJT/settings.py
  
  INSTALLED_APPS = [
    'app1',
    'django_extensions',
  ]
  ```

- *참고*

  - `IPython`

    - 파이썬 기본 쉘보다 더 강력한 파이썬 쉘
    - django-extensions

  - `django-extensions`

    - Django 확장 프로그램 모음
    - `shell_plus`, `graph model` 등 다양한 확장 기능 제공

  - `Shell`

    - 운영체제 상에서 다양한 기능과 서비스를 구현하는 인터페이스를 제공하는 프로그램
    - 사용자와 운영 체제의 내부사이의 인터페이스를 감싸는 층이기 때문에 `Shell(껍데기)`라는 이름이 붙음
    - '사용자 ⬌ 셸 ⬌ 운영체제'

  - `Python Shell`

    - 파이썬 코드를 실행해주는 인터프리터

      > 인터프리터 : 코드를 한 줄씩 읽어 내려가며 실행하는 프로그램

    - 인터렉티브 혹은 대화형 shell이라고 부름

    - Python 명령어를 실행하여 그 결과를 바로 제공

    ```zsh
    python
    ```

  - `Django shell`

    - ORM 관련 구문 연습을 위해 파이썬 쉘 환경을 사용
    - 다만 일반 파이썬 쉘을 통해서는 장고 프로젝트 환경에 영향을 줄 수 없기 때문에 Django 환경 안에서 진행할 수 있는 Django shell을 사용
    - 원래는 다음과 같은 명령어를 통해 Django shell을 사용하지만

    ```zsh
    python manage.py shell
    ```

    ​		`Django-extension`이 제공하는 더 강력한 `shell_plus`로 진행

    ```zsh
    python manage.py shell_plus
    ```

***

#### 📃 Database API

- `Database API의 구문`

  - <span style='background-color: #ffdce0'>App1</span>.<span style='background-color: #fff561'>objects</span>.<span style='background-color: #dcffe4'>all()</span>

    <span style='background-color: #ffdce0'>Model class</span>.<span style='background-color: #fff561'>Manager</span>.<span style='background-color: #dcffe4'>Queryset API</span>

- `Objects manager`

  - Django 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스
  - Django는 기본적으로 모든 Django 모델 클래스에 대해 `objects`라는 `Manager` 객체를 자동으로 추가함
  - 이 `Manager`를 통해 특정 데이터를 조작할 수 있음
  - DB를 `python class`로 조작할 수 있게 여러 메서드를 제공하는 `manager`

- `Query`

  - 데이터베이스에 특정한 데이터를 보여달라는 요청
  - 파이썬으로 작성한 코드가 OMR에 의해 SQL로 변환되어 데이터베이스에 전달되며 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달

- `QuerySet`

  - 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
    - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
  - Django ORM을 통해 만들어진 자료형이며 필터를 걸거나 정렬 등을 수행할 수 있음
  - `objects manager`를 사용하여 복수의 데이터를 가져오는 `queryset method`를 사용할 때 반환되는 객체
  - 단, 데이터베이스가 단일한 객체를 반환할 때는 `QuerySet`이 아닌 모델(`Class`)의 인스턴스로 반환됨

***

#### 📃 QuerySet API 익히기

- `CRUD`
  - `Create` / `Read` / `Update` / `Delete`
    - 생성 / 조회 / 수정 / 삭제
  - 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능 4가지를 묶어서 일컫는 말

***

#### 📃 CREATE

- 데이터 객체를 생성하는 첫번째 방법
  1. `app1 = App1()`
     - 클래스를 통한 인스턴스 생성
  2. `app1.title = 'first'`
     - 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당
  3. `app1.save()`
     - 인스턴스로 save 메서드 호출
- 데이터 객체를 생성하는 두번째 방법
  1. `app1 = App1(title='first', content='django')`
     - 인스턴스 생성시 초기값을 함께 작성하여 생성
  2. `app1.save()`
     - save 메서드를 호출해서 저장
- 데이터 객체를 생성하는 세번째 방법
  - `QuerySet API` 중 `create()` 메서드 활용

```zsh
# 위의 2가지 방법과는 다르게 바로 생성된 데이터가 반환됨
App1.objects.create(title='first', content='django')
```

- `save()`
  - 'Saving object'
  - 객체를 데이터베이스에 저장함
  - 데이터 생성시 save를 호출하기 전에는 객체의 id 값은 None
  - 단순히 모델 클래스를 통해 인스턴스를 생성하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save를 호출해야 테이블에 레코드가 생성됨

***

#### 📃 READ

- `all()`

  - QuerySet return
  - 전체 데이터 조회

  ```zsh
  App1.objects.all()
  ```

- `get()`

  - 단일 데이터 조회
  - 객체를 찾을 수 없으면 `DoesNotExist` 예외를 발생, 둘 이상의 객체를 찾으면 `MultipleObjectsReturned` 예외 발생
  - 위와 같은 특징을 가지고 있기 때문에 `primary key`와 같이 고유성(`uniqueness`)을 보장하는 조회에서 사용해야 함

  ```zsh
  App1.objects.get(pk=1)
  # <App1: App1 object(1)>
  App1.objects.get(pk=100)
  # DoesNotExist
  App1.objects.get(content='django')
  # MultipleObjectsReturned
  ```

- `filter()`

  - 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet을 반환

  ```zsh
  App1.objects.filter(content='django')
  # <QuerySet [<App1: App1 object(1)>, <App1: App1 object(2)>, <App1: App1 object(3)>]>
  App1.objects.filter(title='MTC')
  # <QuerySet []>
  App1.objects.filter(title='first')
  # QuerySet [<App1: App1 object (1)]>
  ```

  > 조회된 객체가 없거나 1개여도 QuerySet을 반환

- `Field lookups`

  - 특정 레코드에 대한 조건을 설정하는 방법
  - QuerySet 메서드 `filter()`, `exclude()`, `get()`에 대한 키워드 인자로 지정됨
  - 예

  ```zsh
  # content 컬럼에 dj가 표함된 모든 데이터 조회
  App1.objects.filter(content__contains='dj')
  ```

***

#### 📃 UPDATE

- `과정`

  - 수정하고자 하는 `app1` 인스턴스 객체를 조회 후 반환값을 저장
  - `app1` 인스턴스 객체의 인스턴스 변수값을 새로운 값으로 할당
  - `save()` 인스턴스 메서드 호출

  ```zsh
  app1 = App1.objects.get(pk=1)
  
  # 인스턴스 변수 변경
  app1.title = 'bye'
  
  # 저장
  app1.save()
  
  # 변경 확인
  app1.titls
  > 'bye'
  ```

***

#### 📃 DELETE

- 삭제하고자 하는 `app1` 인스턴스 객체를 조회 후 반환값을 저장

- `delete()` 인스턴스 메서드 호출

  ```zsh
  app1 = App1.objects.get(pk=1)
  
  # delete 메서드 호출
  app1.delete()
  
  # 이제 1번 데이터는 조회할 수 없음
  App1.objects.get(pk=1)
  > DoesNotExist
  ```

