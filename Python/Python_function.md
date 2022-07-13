# 함수(function)

- 함수란?

  - 특정한 기능을 하는 코드의 조각(묶음)
  - 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고 필요시에만 호출하여 간편하게 사용

- 정의

  - 사용자 함수(Custom Function)
    - 구현되어 있는 함수가 없는 경우 사용자가 직접 함수를 작성 가능

  ```python
  def function_name
      # code block
      return returning_value
  ```

  

- 함수를 왜 사용할까?

  - **Decomposition** 기능을 분해, 재사용 가능

  ```python
  numbers = [1, 10, 100]
  result = 0
  cnt = 0
  for number in numbers:
      result += number
      cnt += 1
  print(result/cnt)
  ```

  ```python
  print(sum(numbers)/len(numbers))
  ```

  - **Abstraction** 복잡한 내용을 숨기고, 기능에 집중하여 사용할 수 있음.

    재사용성, 가독성, 생산성

    *블랙박스 : 안에 어떠한 것이 있는지는 모르지만*

    *추상 : 사물이 지니고 있는 여러가지 측면 가운데서 특정한 측면만을 가려내어 포착하는 것*

- 내장함수(Bulit-in Function) 활용







## 함수의 기초

- 선언과 호출

  - 선언은 `def` 키워드 활용

  - 들여쓰기를 통해 function body(실행될 코드 블록)을 작성

    - Docstring은 함수 body 앞에 선택적으로 작성

      ❗️*작성시에는 반드시 첫번째 문장에 문자열 `" "` 작성*

  - parameter를 넘겨줄 수 있음

  - 동작 후에 `return` 을 통해 결과값을 전달

  - `'함수명'()` 으로 호출

    - parameter가 있는 경우, 함수명(값1, 값2, ...)로 호출

    ```python
    def foo(): #호출
      return True
    
    def add(x, y):
      return x + y
    ```

  - 예시

  ```python
  num1 = 0
  num2 = 1
  
  def func1(a, b):
      return a + b
      
  def func2(a, b):
      return a - b
      
  def func3(a, b):
      return func1(a, 5) + func2(5, b)
      
  result = func3(num1, num2)
  print(result) # 9
  ```







## 함수의 결과값(output)

- 반드시 값을 하나만 return 한다.
  - 명시적인 return이 없는 경우에도 None을 반황
- return과 동시에 실행 종료



- 아래 코드의 문제점은 무엇일까?

```python
def minus_and_product(x, y):
    return x - y # 실행 후 종료
    return x * y # 실행되지 않음
```

- 두 개 이상의 값을 반환하는 방법
  - 튜플 반환(vs code에서 타입 찍어보기)

```python
def minus_and_product(x, y):
    return x - y, x * y
```



💡**return vs print**

- return은 함수 안에서 값을 반환하기 위해 사용되는 **키워드**
- print는 출력을 위해 사용되는 **함수**







## 함수의 입력(Input)

- Parameter : 함수를 실행할 때 함수 내부에서 사용되는 식별자
- Argument : 함수를 호출할 때 넣어주는 값

```python
def function(ham): # parameter : ham
    return ham
    
function('spam') # Argument
```

- Argument란?

  - 함수 호출시 함수의 파라미터를 통해 전달되는 값

  - Argument 소괄호 안에 할당 func_name(argument)

    - 필수 Argument : 반드시 전달되어야 하는 Argument
    - 선택 Argument : 값을 전달하지 않아도 되는 

  - positional Argument*(기본)*

    - 기본적으로 함수 호출시 Argument는 위치에 따라 함수 내에 전달됨

    ```python
    def add(x, y):
      return x + y
    
    add(2, 3)
    
    # 2 -> x
    # 3 -> y
    ```

  - Keyword Argument

    - 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
    - keyword Argument 다음에 positional Argument를 활용할 수 없음 *반대는 사용 가능*

    ```python
    def add(x, y):
        return x + y
        
    add(x=2, y=5)
    add(2, y=5)
    add(y=5, x=2)
    
    # add(x=2, 5)로는 사용할 수 없음
    ```

  - Default Argument Values

    - 기본값을 지정하여 함수 호출시 Argument 값을 설정하지 않도록 함
      - 정의된 것보다 더 적은 개수의 Argument들로 호출될 수 있음

    ```python
    def add(x, y = 0):
      return x + y
    
    add(2)
    ```

  - 정해지지 않은 개수의 Argument

    - 여러 개의 positional Argument를 하나의 필수 parameter로 받아서 사용
      - 몇 개의 positional Argument를 받을지 모르는 함수를 정의할 때 유용
    - Argument들은 튜플로 묶어 처리되며 parameter에 `*` 를 붙여 표현

    ```python
    def add(*args):
      for arg in args:
      print(arg)
      
    add(2)
    add(2, 3, 4, 5)
    ```

  - 정해지지 않은 개수의 keyword Argument

    - 임의의 개수 Argument를 keword Argument로 호출될 수 있도록 지정
    - Argument들은 딕셔너리로 묶여 처리되며 parameter에 `**` 를 붙여 표현

    ```python
    def students(**kwargs):
      for key, value in kwargs:
        print(key, ":", value)
        
    students(std1 = '영희', std2 = '철수', std3 = '만수')
    ```

    





## 함수의 범위(Scope)

- 함수는 코드 내부에 local scope를 생성하며 그 외의 공간인 global scope로 구분
  - scope
    - Global scope : 코드 어디에서든 참조할 수 있는 공간
    - Local scope : 함수가 만든 scope. 함수 내에서만 참조 가능
  - variable
    - global variable : Global scope에 정의된 변수
    - local variable : Local scope에 정의된 변수

- 객체 수명주기(lifecycle)

  - built-in scope
    - 파이썬이 실행된 이후부터 영원히 유지
  - global scope
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  - Local scope
    - 함수가 호출될 때 생성되고 함수가 종료될 때까지 유지
  - 예시

  ```python
  def func():
    a = 20
    print('local', a)
    
  func()
  print('global', a)
  
  # local 20
  
  # 3 print('local', a)
  # 5 func() ---->
  # 6 print('global', a)
  # NameError : name 'a' is not defined
  
  # a는 Local scope에서만 존재
  ```

  

- 이름 검색 규칙(name resolution)

  - 파이썬에 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
  - 아래와 같은 순서로 이름을 찾아나가며 `LEGB Rule` 이라고 부름
    - Local scope : 함수
    - Enclosed scope : 특정 함수의 상위 함수
    - Global scope : 함수 밖의 변수, Import 모듈
    - Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성
  - 즉, 함수 내에서는 바깥 scope의 변수에 접근은 가능하지만 수정은 할 수 없음
  - 예시

  ```python
  print(sum)
  print(sum(range(2)))
  sum = 5
  print(sum)
  print(sum(range(2)))
  
  # <Built-in function sum>
  # 1
  # 5
  
  ---------------------------
  
  # TypeError Traceack (most recent call last)
  # 3. sum = 5
  # 4. print(sum) ------>
  # 5. print(sum(range(2)))
  # TypeError: 'int' object is not callable
  ```

  





## 함수 응용

- map(function, iterable)

  - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용하고

    그 결과를 map object로 반환

  ```python
  numbers = [1, 2, 3]
  result = map(str, numbers)
  print(result, type(result))
  # <map object at 0x10e2ca100> <class 'map'>
  
  list(result) # 리스트 형변환을 통해 결과 직접 확인
  ```

  - 알고리즘 문제 풀이시 input 값들을 숫자로 바로 활용하고 싶을 때

  ```python
  n, m = map(int, input().split())
  # 3 5
  
  print(n, m)
  print(type(n), type(m))
  # 3 5
  # <class 'int'> <class 'int'>
  ```

  