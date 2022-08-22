### `입력&출력`

----------

#### 🔎 입력 활용 예시(input)

- `input()` 은 사용자의 입력 한 줄을 문자열로 받는 함수

  ```python
  word = input()
  >>> happycat
  ```

  > word ➡︎ "happycat"

- `input()` 과 `map` 함수를 이용해 원하는 대로 입력 받기

  ```python
  # 문자열 입력 받기
  a = input()
  
  # 한 개 숫자 입력 받기
  b = int(input())
  c = float(input())
  
  # 여러 개 숫자 입력 받기
  d, e = map(int, input().split())
  f, g, h = map(float, input().split())
  ```

- 파이썬의 내장 함수 map(*function, iterable*)

  ```python
  map(int, ['1', '2', '3']) # 각 원소에 int를 적용
  # ➡︎ 정수 1, 2, 3을 반환
  
  map(float, [1, 2, 3]) # 각 원소에 float를 적용
  # ➡︎ 부동소수점 1.0, 2.0, 3.0을 반환
  
  map(int, '123') # 각 원소에 int를 적용
  # ➡︎ 리스트 뿐만 아니라 문자열에도 적용 가능. 정수 1, 2, 3을 반환
  ```



#### 🔎 출력 활용 예시(print)

- `print()`는 데이터를 출력할 수 있는 함수이며 자동적으로 줄 바꿈 발생

  ```python
  print('happy')
  print('cat')
  >>> happy
  >>> cat
  ```

- `콤마(,)`를 이용해 여러 인자를 넣으면 공백을 기준으로 출력

  ```python
  a = 'happy'
  b = 'cat'
  
  print(a, b)
  >>> happy cat
  ```

- `end`, `sep` 옵션을 사용하여 출력 조작하기

  ```python
  a = 'happy'
  b = 'cat'
  
  print(a, end = '@')
  print(b)
  >>> happy@cat
  
  print(a, b, sep = '\n')
  >>> happy
  >>> cat
  ```

  