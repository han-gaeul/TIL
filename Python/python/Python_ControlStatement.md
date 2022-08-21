#### ```제어문 (Control Statement)```

-------------------------

- 특정 상황에 따라 코드를 선택적으로 실행하거나 계속하여 실행(반복)하는 제어가 필요

- 순서도(flow chart)로 표현 가능



##### 조건문

- 참/거짓을 판단할 수 있는 조건식과 함께 사용

- 기본 형식
  - Expression에는 참/거짓에 대한 조건식
    - else는 선택적으로 활용 가능

```python
if 'ex' :
    # Run this code block <- 참일때 실행
else:
    # Run this code block <- 거짓일때 실행
```

- 예시

```python
a = -10
if a >= 0:
    print('양수')
else:
    print('음수')
print(a)
# '음수'
```

- 실습 문제
  - 조건문을 통해 변수 num의 값의 홀수/짝수 여부를 출력

```python
# 내가 작성한 코드
num = int(input())
if %2 == 1:
    print('홀수')
else:
    pritn('짝수')
print(num)
```

```python
# 풀이
# 1. num은 input으로 사용자에게 입력 받기
num = int(input()) # input으로 받는 기본 타입은 문자열!!
# print(num)
# 2. 조건문을 통해서 홀수/짝수 여부를 출력
# 숫자로서의 num!
if num % 2 == 1: #int(num)으로 작성 가능
    print('홀수')
else:
    print('짝수')
```



##### 복수 조건문

- **elif**

```python
if 'ex':
    # code block
elif 'ex':
    # code block
else:
    code block
```

- 실습 문제
  - 다음은 미세먼지 농도에 따른 등급일 때, dust 값에 따라 등급을 출력하는 조건식을 작성하시오.

```python
# 내가 작성한 코드
dust = int(input())
if dust < 30:
    print('미세먼지 농도 : 좋음')
elif dust < 80:
    print('미세먼지 농도 : 보통')
elif dust < 150:
    print('미세먼지 농도 : 나쁨')
else:
    print('미세먼지 농도 : 매우나쁨')
```

```python
# 풀이
dust = 100

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
# else는 위의 모든 조건에 해당하지 않는 나머지의 경우이기에 별도의 조건은 불가능
# else에는 조건문 '절대로' 작성하지 않음!!
# 조건문에서 else는 생략 가능
else:
    print('좋음')
print('미세먼지 확인 완료')
```



❗️조건식을 동시에 검사하는 것이 아니라 순차적으로 비교함



##### 중첩 조건문

- 조건문은 다른 조건문에 중첩되어 사용 가능
  - 들여쓰기를 유의하여 작성!

```python
if 'ex':
    # code block
    if 'ex':
        # code block
else:
    print()
```

- 실습 문제

  - 아래의 코드에서 중첩 조건문을 활용하여 미세먼지 농도(dust값)이 300이 넘는 경우 '실외 활동을 자제하세요.'를 추가적으로 출력하고 음수인 경우 '값이 잘못 되었습니다.'를 출력하시오.

  ```python
  dust = -10
  
  if dust > 150:
      if dust > 300:
          print('실외 활동을 자제하세요.')
      print('매우 나쁨')
  elif dust > 80:
      print('나쁨')
  elif dust > 30:
      print('보통')
  else:
      if dust >= 0:
          print('좋음')
      else:
          print('값이 잘못 되었습니다.')
          
  # else 가 없으면 동시 출력, else가 있으면 동시 출력 되지 않음
  
  # 아래 코드처럼 작성 가능
  #elif dust > 0:
  #    print('좋음')
  #else:
  #    print('음수 값입니다.')
  ```



##### 조건 표현식(Conditional Expression)

- 일반적으로 조건에 따라값을 할당할 때 활용

```python
<True인 경우의 값> if <expression> else <false인 경우의 값>
```



- 실습 문제
  - num이 정수일 때, 아래의 코드는 무엇을 위한 코드일까?

```python
value = num # 참일 경우
if num >= 0 # 'ex'
else -num # 거짓일 경우

# 절대값을 구하는 코드
```

- 실습 문제 2

```python
num = int(input())
value = num if num >= else -num
print(value)

# 절대값 계산기
```

- 실습 문제 3
  - 다음의 코드와 동일한 조건 표현식을 작성하시오.

```python
num = 2
if num % 2:
    result = '홀'
else:
    result = '짝'
print(result)
```

```python
num = 2
result = '홀' if num % 2 else '짝'
print(result)
```

- 실습 문제 4
  - 다음의 코드와 동일한 조건문을 작성하시오.

```python
num = -5
value = num if num >= 0 else 0
print(value)
```

```python
num = -5
if num >= 0:
  value = num
else:
  value = 0
print(value)
```







##### 반복문

- 특정 조건에 도달할 때까지 계속 반복되는 일련의 문장
- 종류

  - while문 : 종료조건에 해당하는 코드를 통해 반복문을 종료시켜야 함
  - for문 : 반복가능한 객체를 모두 순회하면 종료(별도의 종료조건이 필요 없음)
  - 반복 제어 : break, continue, for-else

- while

  - 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행
  - 코드 블록이 모두 실행되고 다시 조건식을 검사하며 반복적으로 실행
  - 무한 반복되지 않도록 종료조건이 반드시 필요함

  ```python
  while 'ex':
      # code block
  ```

  ```python
  # 이 코드가 실행되는 횟수는?
  a = 0
  while a < 5:
      print(a)
      a += 1
  print('끝')
  #5번
  ```

- 실습 문제

  - 1부터 사용자가 입력한 양의 정수까지의 총합을 구하는 코드를 작성하시오.

  ```python
  # 값 초기화
  n = 0
  total = 0
  user_input = int(intput())
  ```

  ```python
  while n <= user_input:
      total += n
      n += 1
  print(totla)
  ```



- for문

  - 시퀀스(string, tuple, list, range)를 포함한 순회 가능한 객체(iterable) 요소를 모두 순회
    - 처음부터 끝까지 모두 순회하므로 별도의 종료 조건이 필요 없음

  ```python
  for '변수명' in 'interable':
    # code block
  ```

  - 일반 형식

    - Iterable

      - 순회할 수 있는 자료형(str, list, dict 등)
      - 순회형 함수(range, enumerate)

    - 문자열 순회

      - 사용자가 입력한 문자를 한 글자씩 세로로 출력하시오.

      ```python
      chars = input()
      # input = hello
      ```

      ```python
      for char int chars:
          print(char)
      # h
      # e
      # l
      # l
      # o
      ```

    - 문자열(String) 순회

      - 사용자가 입력한 문자를 `range` 를 활용하여 한 글자씩 출력하시오.

      ```python
      chars = input()
      # input = hello
      ```

      ```python
      for i in range(len(chars)):
        print(chars[i0])
      # h
      # e
      # l
      # l
      # o
      ```

    - enumerate 순회

      - Enumerate()

        - 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환

          - (index, value) 형태의 tuple로 구성된 열거 객체를 반환

          ```python
          members = ['민수', '영희', '철수']
          
          for i in range(len(members)):
              print(f'{i} {members[i]}')
          ```

          ```python
          for i, member in enumrate(members):
            print(i, member)
          ```

          ```python
          enumerate(members) # <enuberate at 0x105d3e100>
          list(enumerate(members))
          # [(0, '민수'), (1, '영희'), (2, '철수') <- 숫자와 값의 tuple
          list(enumerate(members, start=1))
          # [(1, '민수'), (2, '영희'), (3, '철수')]
          # 기본값 0, start를 지정하면 해당 값부터 순차적으로 증가
          ```

    - 딕셔너리 순회

      - 기본적으로 key를 순회하며 key를 통해 값을 활용

      ```python
      grades = {'영희':90, '철수':80}
      for name in grades:
        print(name)
      
      # 영희
      # 철수
      ```

      ```python
      grades = {'영희':90, '철수':80}
      for name in grades:
        print(name, grades[name])
        
      # 영희 90
      # 철수 80
      ```

      

##### 반복문 제어

- Break : 반복문 종료

```python
n = 0
while True:
  if n == 3:
    break
  print(n)
  n += 1

# 0
# 1
# 2
```

```python
for i in range(10):
  if i > 1:
    print('0과 1만 출력해줘')
    break
  print(i)

# 0
# 1
# 0과 1만 출력해줘
```

- Continue : continue 이후의 코드 블록은 수행하지 않고 다음 반복을 수행

```python
for i in range(6):
  if i % 2 == 0:
    continue
  print(i)
  
# 1
# 3
# 5
```

- For-else : 끝까지 반복문을 실행한 이후에 else문 실행
  - Break를 통해 중간에 종료되는 경우 else문은 실행되지 않음

```python
for x in 'apple':
  if x == 'b':
    print('b!')
    break
else:
  print('b가 없습니다.')

# b가 없습니다.
```

```python
for x in 'banana':
  if x == 'b':
    print('b!')
    break
else:
  print('b가 없습니다.')

# b!
```



💡[Python Tutor](https://pythontutor.com/visualize.html#mode=edit) 사이트를 통해 코드가 돌아가는 모습을 직관적으로 볼 수 있음
