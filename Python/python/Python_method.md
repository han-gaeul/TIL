### ``` 메서드(method)```

-------------------------------

##### 시퀀스 - 순서가 있는 데이터 구조

- 문자열

  - 문자들의 나열(sequence of characters)

    - 모든 문자는 str 타입

  - 작은 따옴표나 큰 따옴표를 활용하여 표기

    - 문자열을 묶을 때 동일한 기호 활용

  - 탐색/검증

    - **.find(x)**

      - x의 **첫 번째** 위치 반환. 없으면 `-1` 반환

      ```python
      'apple'.find('p') # 1
      'apple'.find('k') # -1
      ```

    - **.index(x)**

      - x의 첫 번째 위치 반환. 없으면 오류 발생

      ```python
      print('apple'.index('p')) # 1
      'apple'.index('k')
      # ------------------------------
      # ValueError Traceback (most recent call last)
      # ----> 1 'apple'.index('k')
      # ValueError: substring not founf
      ```

    - 검증 메소드

    ```python
    'abc'.isalpha() # True. 알파벳
    'Ab'.isupper() # False. 대문자
    'ab'.islower() # True. 소문자
    'Title Title'.istitle() # True. 앞글자가 대문자
    ```

    

  |    문법     | 설명                                                         |
  | :---------: | :----------------------------------------------------------- |
  |  s.find(x)  | x의 첫 번째 위치 반환. 없으면 `-1` 을 반환                   |
  | s.index(x)  | x의 첫 번째 위치 반환. 없으면 오류 발생                      |
  | s.isalpha() | 알파벳 문자 여부. <br />*단순 알파벳이 아닌 유니코드상 letter(한국어도 포함)* |
  | s.isupper() | 대문자 여부                                                  |
  | s.islower() | 소문자 여부                                                  |



- 문자열 변경

  - **.replace(old, new[,count])**

    - 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
    - count를 지정하면 해당 개수만큼만 시행

    ```python
    'coone'.replace('o', 'a') # caane
    'wooooowoo'.replace('o', '!', 2) # w!!ooowoo
    ```

    - **.strip([chars]) **
      - 특정한 문자들을 지정
      - 양쪽을 제거하거나(strip), 왼쪽을 제거하거나(strip), 오른쪽을 제거(rstrip)
      - 문자열을 지정하지 않으면 공백 제거. *공백에는 space, '\n' 포함*

    ```python
    '    와우\n'.strip() # '와우'
    '    와우\n'.lstrip() # '와우\n'
    '    와우\n'.rstrip() # '    와우'
    '안녕????'.rstrip('?') # '안녕'
    ```

    - **.split(sep=None, maxsplit=-1)**

      - 문자열을 특정한 단위로 나눠 **리스트로 반환**

        - sep이 None이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주

          선행/후행 공백은 빈 문자열에 포함X

        - maxsplit이 -1인 경우 제한X

    ```python
    'a, b, c'.split('-') # ['a, b, c']
    'a, b, c'.split() # ['a', 'b', 'c']
    ```

    - **'separator'.join([iterable])**
      - 반복 가능한(iterable) 컨테이너 요소들을 separator(구분자)로 합쳐 **문자열 반환**
        - iterable에 **문자열이 아닌 값이 있으면 TypeError 발생**

    ```python
    ''.join(['3', '5']) # 35
    ```

  

  |               문법               | 설명                                                         |
  | :------------------------------: | :----------------------------------------------------------- |
  |  s.replace(*old, new[,count]*)   | 바꿀 대상의 글자를 새로운 글자로 바꿔서 반환<br />count를 지정하면 해당 개수만큼만 적용 |
  |        s.strip(*[chars]*)        | 특정한 문자를 지정하면<br />양쪽을 제거하거나(strip), 왼쪽을 제거하거나(lstrip), 오른쪽을 제거(rstrip)<br />문자열을 지정하지 않으면 공백을 제거함 |
  | s.split(*sep=None, maxsplit=-1*) | 문자열을 특정한 단위로 나눠 리스트로 반환                    |
  | *'separator'*.join(*[iterable]*) | 반복 가능한 컨테이너 요소들을 seperator(구분자)로 합쳐 문자열 반환<br />() 안에 문자열이 아닌 값이 있으면 TypeError 발생 |
  |          s.capitalize()          | 가장 첫 번째 글자를 대문자로 변경                            |
  |            s.title()             | `'` 나 공백 이후를 대문자로 변경                             |
  |            s.upper()             | 모두 대문자로 변경                                           |
  |            s.lower()             | 모두 소문자로 변경                                           |
  |           s.swapcase()           | 대소문자 서로 변경                                           |

  

❗️*문자열은 스스로 바뀌는 경우X **immutable***

​	 *모두 바뀐 결과를 반환한다.*



##### 리스트

- 변경 가능한(mutable) 값들의 자료형, 반복 가능(iterable) *스스로 변경 가능*
- 순서를 가지며 서로 다른 타입의 요소를 가질 수 있음
- 항상 **대괄호** 형태로 정의. 요소는 콤마로 구분

|         문법          | 설명                                                         |
| :-------------------: | :----------------------------------------------------------- |
|      L.append(x)      | 리스트 마지막에 항목 x를 추가                                |
|    L.insert(i, x)     | 리스트 인덱스 i에 항목 x를 삽입                              |
|      L.remove(x)      | 리스트 가장 왼쪽에 있는 항목*(첫 번째)* x 제거<br />항목이 존재하지 않으면 ValueError |
|        L.pop()        | 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거        |
|       L.pop(i)        | 리스트의 인덱스 i에 있는 항목을 반환 후 제거                 |
|  L.expend(iterable)   | ()안의 항목 추가<br />여러 개를 추가하려면 리스트로 묶어서 넣어야 함<br />문자열 'banana' 를 넣으면 'b', 'a', 'n', 'a', 'n', 'a' 이렇게 추가 |
| L.inde(x, start, end) | 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환 |
|      L.reverse()      | 순서를 반대로 뒤집음(정렬 X). None 반환                      |
|       L.sort()        | 원본 리스트를 정렬. None 반환<br />!= sorted                 |
|      L.count(x)       | 리스트에서 항목 x가 몇 개 존재하는지 갯수 반환               |

- **.append(x)**

  - 리스트에 값 추가하기

  ```python
  cafe = ['star', 'tom', 'holl']
  # 'star', 'tom', 'holl'
  cafr.append('bana')
  #['star', 'tom', 'holl', 'bana']
  ```

- **.extend(iterable)**

  - 리스트에 iterable의 항목 추가

  ```python
  cafe = ['star', 'tom', 'holl']
  # 'star', 'tom', 'holl'
  cafr.extend(['cafe', 'test'])
  #['star', 'tom', 'holl', 'cafe', 'test']
  ```

- **.insert(i, x)**

  - 정해진 위치 i에 값 추가

  ```python
  cafe = ['star', 'tom', 'holl']
  # 'star', 'tom', 'holl'
  cafr.insert(0, 'start')
  # ['star', 'star', 'tom', 'holl']
  ```

  ```python
  cafe = ['star', 'tom', 'holl']
  # 'star', 'tom', 'holl'
  cafr.insert(10000, 'start')
  # ['star', 'tom', 'holl', 'start']
  # 리스트 길이보다 큰 경우 맨 뒤에 추가
  ```

- remove(x)

  - 리스트에서 값이 x인 것 삭제

  ```python
  numbers = [1, 2, 3, 'hi']
  # [1, 2, 3, 'hi']
  numbers.reamove('hi')
  # [1, 2, 3]
  ```

  ```python
  numbers.reamove('hi')
  # ---------------------
  # 없는 경우 ValueError
  # ValueError Traceback (most recent call last)
  # -----> 1 numbers.remove('hi')
  # ValueError: list.remove(x): x not in list
  ```

- .pop(i)

  - 정해진 위치 i에 잆는 값 삭제하고 반환
  - i가 지정되지 않으면 마지막 항목을 삭제하고 반환

  ```python
  numbers = ['hi', 1, 2, 3]
  # ['hi', 1, 2, 3]
  pop_number = number.pop()
  print(pop_number) # 3
  print(numbers) # ['hi', 1, 2]
  ```

  ```python
  numbers = ['hi', 1, 2, 3]
  # ['hi', 1, 2, 3]
  pop_number = number.pop(0)
  print(pop_number) # hi
  print(numbers) # [1, 2, 3]
  ```

- .clear()

  - 모든 항목 삭제

  ```python
  numbers = [1, 2, 3]
  print(numbers.clear())
  # []
  ```

- inde(x)

  - x값을 찾아 해당 index 값 반환

  ```python
  numbers = [1, 2, 3, 4]
  print(numbers.index(3)) # 2
  print(numbers.index(100))
  # --------------------------
  # ValueError Traceback (most recent call last)
  # ----> 4 print(numbers.index(100))
  # ValueError: 100 is not in list
  ```

- .count(x)

  - 원하는 값의 개수 반환

    *리스트를 순회하며(for문) 값이 1인 것을 cnr += 1(if문)*

  ```python
  numbers = [1, 2, 3, 1, 1]
  print(numbers.count(1)) # 3
  print(numbers.count(100)) # 0
  ```

- .sort()

  - 원본 리스트를 정령하고 none 반환
  - sorted 함수와 비교

  ```python
  numbers = [3, 2, 5, 1]
  result = numbers.sort()
  print(numbers, result)
  # 원본 변경
  # [1, 2, 3, 5] None
  ```

  ```python
  number = [3, 2, 5, 1]
  result = sorted(numbers)
  print(numbers, result)
  # 정렬된 리스트를 반환. 원본 변경 없음
  # [3, 2, 5, 1] [1, 2, 3, 5]
  ```

- .reverse()

  - 순서를 반대로 뒤집음(정렬X)
  - None 반환

  ```python
  numbers = [3, 2, 5, 1]
  result = numbers.reverse()
  print(numbers, result)
  # [1, 5, 2, 3] None
  ```

  

##### 컬렉션 - 순서가 없는 데이터 구조

- 세트(set)

  - 유일한 값들의 모음(collection)

  - 순서가 없고 중복된 값이 없음. 집합 연산 가능

  - 변경 가능(mutable), 반복 가능(iterable)

    ❗️ 세트는 순서가 없어서 반복의 결과가 정의한 순서와 다를 수 있음

  |      문법       | 설명                                                         |
  | :-------------: | :----------------------------------------------------------- |
  |    s.copy()     | 세트의 얕은 복사본 반환                                      |
  |    s.add(x)     | 항목 x가 세트 s에 없다면 추가                                |
  |     s.pop()     | 세트 s에서 랜덤하게 항목을 반환하고 해당 항목 제거. 세트가 비어있을 경우 KeyError |
  |   s.remove(s)   | 항목 x를 세트 s에서 삭제. 항목이 존재하지 않을 경우 KeyError |
  |  s.discard(x)   | 항목 x가 세트 s에 있는 경우 항목 x를 세트 s에서 삭제         |
  |   s.update(t)   | 세트 t에 있는 모든 항목 중 세트 s에 없는 항목을 추가         |
  |    s.clear()    | 모든 항목을 제거                                             |
  | s.isdisjoint(t) | 세트 s가 세트 t의 서로 같은 항목을 하나라도 갖고 있지 않으면 True 반환 |
  |  s.issubset(t)  | 세트 s가 세트 t의 하위 세트인 경우 True 반환                 |
  | s.issuperset(t) | 세트 s가 세트 t의 상위 세트인 경우 True 반환                 |

  

- 딕셔너리

  - 조회

    - .get(key[,default])
      - key를 통해 value를 가져옴
      - keyerror가 발생하지 않음. default값을 설정할 수 있음(기본 : none)

    ```python
    my_dict = {'apple':'사과', 'banana':'바나나'}
    my_dict['pineapple']
    # ----------------------
    # KeyError Traceback (mosi recent call last)
    # ----> 2 my_dict['pineapple']
    # KeyError: 'pineapple'
    ```

    ```python
    my_dict = {'apple':'사과', 'banana':'바나나'}
    print(my_dict.get('pineapple')) # None
    print(my_dict.get('apple')) # 사과
    print(my_dict.get('pineapple', 0)) # 0
    ```

    - .pop(key[,default])
      - key가 딕셔너리에 있으면 제거하고 해당 값 반환
      - 그렇지 않으면 default 반환
      - default값이 없으면 KeyError

    ```python
    my_dict = {'apple':'사과', 'banana':'바나나'}
    data = my_dict.pop('apple')
    print(data, my_dict)
    # 사과 {'banana':'바나나'}
    ```

    - .update([other])
      - 값을 제공하는 key, value로 덮어씀

    ```python
    my_dict = {'apple':'사', 'banana':'바나나'}
    my_dict.update(apple='사과')
    print(my_dict)
    # {'apple':'사과', 'banana':'바나나'}
    ```

  
  | 문법                 | 설명                                                         |
  | -------------------- | ------------------------------------------------------------ |
  | .get(key[,default])  | key를 통해 value를 가져옴<br />KeyError가 발생하지 않으며 default 값을 설정할 수 있음<br />기본 : None |
  | .pop(key,[,default]) | key가 딕셔너리에 있으면 제거하고 해당 값을 반환<br />그렇지 않으면 default 반환<br />default 값이 없으면 KeyError |
  | .update()            | 값을 제공하는 key, value로 덮어씌움                          |
  | .keys()              | 딕셔너리 d의 모든 키를 담은 뷰 반환                          |
  | .values()            | 딕셔너리 d의 모든 값을 담은 뷰 반환                          |
  | .items()             | 딕셔너리 d의 모든 키-값의 쌍을 담은 뷰 반환                  |
  
  