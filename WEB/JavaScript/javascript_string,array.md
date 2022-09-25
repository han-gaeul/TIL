### `JavaScript - 문자열, 배열`

***

#### 🔎 문자열 (String) 관련 주요 메서드

- `includes`

  - string.includes(value)
  - 문자열에 value가 존재하는지 판별 후 참 또는 거짓 반환

  ```js
  const str = 'a santa at nasa'
  
  str.includes('santa')
  // true
  str.includes('asan')
  // false
  ```

- `split`

  - string.split(value)
  - value가 없을 경우 기존 문자열을 배열에 담아 반환
  - value가 빈 문자열인 경우 각 문자로 나눈 배열을 반환
  - value가 기타 문자열일 경우 해당 문자열로 나눈 배열을 반환

  ```js
  const str = 'a cup'
  
  str.split()
  // ['a cup']
  str.split('')
  // ['a', ' ', 'c', 'u', 'p']
  str.split(' ')
  // 'a', 'cup'
  ```

- `replace`

  - string.replace(from, to)
    - 문자열에 from 값이 존재할 경우 1개만 to 값으로 교체하여 반환
  - string.replaceAll(from, to)
    - 문자열에 from 값이 존재할 경우 모두 to 값으로 교체하여 반환

  ```js
  const str = 'a b c d'
  
  str.replace(' ', '-')
  // 'a-b c d'
  str.replaceAll(' ', '-')
  // 'a-b-c-d'
  ```

- `trim`

  - string.trim()
    - 문자열 시작과 끝의 모든 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환
  - string.trimStart()
    - 문자열 시작의 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환
  - string.trimEnd()
    - 문자열 끝의 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환







#### 🔎 배열 (Arrays)

- 정의와 특징

  - 키와 속성들을 담고 있는 참조 타입의 객체
  - 순서를 보장하는 특징이 있음
  - 주로 대괄호를 이용하여 생성하고 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
  - 배열의 길이는 array.length 형태로 접근 가능
    - *(참고)* 배열의 마지막 원소는 array.length - 1로 접근

  ```js
  const numbers = [1, 2, 3, 4, 5]
  console.log(numbers[0])
  // 1
  console.log(numbers[-1])
  // undefined
  console.log(numbers.length)
  // 5
  ```

  ```js
  const numbers = [1, 2, 3, 4, 5]
  console.log(numbers[numbers.length - 1])
  // 5
  console.log(numbers[numbers.length - 2])
  // 4
  console.log(numbers[numbers.length - 3])
  // 3
  console.log(numbers[numbers.length - 4])
  // 2
  console.log(numbers[numbers.length - 5])
  // 1
  ```

- 관련 주요 메서드

  - `reverse`
    - array.reverse()
    - 원본 배열의 요소들의 순서를 반대로 정렬

  ```js
  const numbers = [1, 2, 3, 4, 5]
  
  numbers.reverse()
  console.log(numbers)
  // [5, 4, 3, 2, 1]
  ```

  - `push & pop`
    - array.push()
      - 배열의 가장 뒤에 요소 추가
    - array.pop()
      - 배열의 마지막 요소 제거

  ```js
  const numbers = [1, 2, 3, 4, 5]
  
  numbers.push(100)
  console.log(numbers)
  // [1, 2, 3, 4, 5, 100]
  
  numbers.pop()
  console.log(numbers)
  // [1, 2, 3, 4, 5]
  ```

  - `unshift & shift`
    - array.unshift()
      - 배열의 가장 앞에 요소 추가
    - array.shift()
      - 배열의 첫번째 요소 제거

  ```js
  const numbers = [1, 2, 3, 4, 5]
  
  numbers.unshift(100)
  console.log(numbers)
  // [100, 1, 2, 3, 4, 5]
  
  numbers.shift()
  console.log(numbers)
  // [1, 2, 3, 4, 5]
  ```

  - `includes`
    - array.includes(value)
    - 배열에 특정 값이 존재하는지 판별 후 참 또는 거짓 반환

  ```js
  const numbers = [1, 2, 3, 4, 5]
  
  console.log(numbers.includes(1))
  // true
  console.log(numbers.includes(100))
  // false
  ```

  - `indexOf`
    - array.indexOf(value)
    - 배열에 특정 값이 존재하는지 확인 후 가장 첫 번째로 찾은 요소의 인덱스 반환
    - 만약 해당 값이 없을 경우 -1 반환

  ```js
  const numbers = [1, 2, 3, 4, 5]
  let result
  
  result = numbers.indexOf(3)
  console.log(result)
  // 2
  
  result = numbers.indexOf(100)
  console.log(result)
  // -1
  ```

  - `join`
    - array.join([separator])
    - 배열의 모든 요소를 연결하여 반환
    - separator(구분자)는 선택적으로 지정 가능하며 생략시 쉼표를 기본 값으로 사용

  ```js
  const numbers = [1, 2, 3, 4, 5]
  let result
  
  result = numbers.join()
  console.log(result)
  // 1, 2, 3, 4, 5
  
  result = numbers.join('')
  console.log(result)
  // 12345
  
  result = numbers.join(' ')
  console.log(result)
  // 1 2 3 4 5
  
  result = numbers.join('-')
  console.log(result)
  // 1-2-3-4-5
  ```

  - `Spread operator`
    - spread operator(...)를 사용하면 배열 내부에서 배열 전개 가능
    - 얕은 복사에 활용 가능

  ```js
  const array = [1, 2, 3]
  const newArray = [0, ...array, 4]
  
  console.log(newArray)
  // [0, 1, 2, 3, 4]
  ```

  - `forEach`
    - array.forEach(callback(element[, index[,array]]))
    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
    - 콜백 함수는 3가지 매개변수로 구성
      - element : 배열의 요소
      - index : 배열 요소의 인덱스
      - array : 배열 자체
    - 반환 값(return)이 없는 메서드

  ```js
  array.forEach((element, index, array) => {
    //code
  })
  ```

  ```js
  const fruits = ['딸기', '수박', '사과', '체리']
  
  fruits.forEach((fruit, index) => {
    console.log(ftuit, index)
    // 딸기 0
    // 수박 1
    // 사과 2
    // 체리 3
  })
  ```

  - `map`
    - array.map(calback(element[, index[, array]]))
    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
    - 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
    - 기존 배열 전체를 다른 형태로 바꿀 때 유용

  ```js
  array.map((element, index, array) => {
    // code
  })
  ```

  ```js
  const numbers = [1, 2, 3, 4, 5]
  
  const doubleNums = numbers.map((num) => {
    return num *2
  })
  
  console.log(doubleNums)
  // [2, 4, 6, 8, 10]
  ```

  - `filter`
    - array.filter(callback(element[, index[, array]]))
    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
    - 콜백 함수의 반환값이 참인 요소들만 모아서 새로운 배열을 반환
    - 기존 배열의 요소들을 필터링할 때 유용

  ```js
  array.filter((element, index, array) => {
    // code
  })
  ```

  ```js
  const numbers = [1, 2, 3, 4, 5]
  
  const oddNums = numbers.filter((num, index) => {
    return num % 2
  })
  console.log(oddNums)
  // 1, 3, 5
  ```

  - `reduce`
    - array.reduce(callback(acc, element, [index[, array]])[, initialValue])
    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
    - 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환
    - reduce 메서드의 주요 매개변수
      - acc
        - 이전 callback 함수의 반환 값이 누적되는 변수
      - initialValue(optional)
        - 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값
    - *(참고)* 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생

  ```js
  array.reduce((acc, element, index, array) => {
    // code
  }, initialValue)
  ```

  ```js
  const numbers = [1, 2, 3]
  
  const result = numbers.reduce((acc, num) => {
    return acc + num
  }, 0)
  console.log(result)
  // 6
  ```

  - `find`
    - array.find(callback(element[, index[, array]]))
    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
    - 콜백 함수의 반환 값이 참이면 조건을 만족하는 첫번째 요소를 반환
    - 찾는 값이 배열에 없으면 undefined 반환

  ```js
  array.find((elemnet, index, array)) {
    // code
  }
  ```

  ```js
  const avengers = [
    { name: 'Tony Stark', age: 45 },
    { name: 'Steve Rogers', age: 32 },
    { name: 'Thor', age:40 }
  ]
  
  const result = avengers.find((avenger) => {
    return avenger.name === 'Tony Stark'
  })
  
  console.log(result)
  // { name: 'Tony Stark', age: 45 }
  ```

  - `some`
    - array.some(callback(element[, index[, array]]))
    - 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환
    - 모든 요소가 통과하지 못하면 거짓 반환
    - *(참고)* 빈 배열은 항상 거짓 반환

  ```js
  array.some((element, index, array) => {
    // code
  })
  ```

  ```js
  const numbers = [1, 3, 5, 7, 9]
  
  const hasEvenNumber = numbers.some((num) => {
    return num % 2 === 0
  })
  console.log(hasEvenNumber)
  // false
  
  const hasEvenNumber = numbers.some((num) => {
    return num % 2
  })
  console.log(hasEvenNumber)
  // True
  ```

  - `every`
    - array.every(callback(element[, index[, array]]))
    - 배열의 모든 요소가 주어진 판별 함수를 통과하면 참을 반환
    - 하나의 요소라도 통과하지 못하면 거짓 반환
    - *(참고)* 빈 배열은 항상 참 반환

  ```js
  array.every((element, index, aray) => {
    // code
  })
  ```

  ```js
  const numbers = [2, 4, 6, 8, 10]
  
  const isEveryNumberEven = numbers.every((num) => {
    return num % 2 === 0
  })
  console.log(isEveryNumberEven)
  // true
  
  const isEveryNumberEven = numbers.every((num) => {
    return num % 2
  })
  console.log(isEveryNumberEven)
  // false
  ```

  