### `JavaScript - 조건문, 반복문, 함수`

***

#### 📝 조건문 종류와 특징

- `'if' statement`

  - 조건 표현식의 결과값을 Boolean 타입으로 변환 후 참/거짓을 판단

  ```js
  const nation = 'Korea'
  
  if (nation === 'Korea') {
    console.log('안녕하세요')
  } else if (nation === 'France') {
    console.log('Bonjour')
  } else {
    console.log('hello')
  }
  ```

- `'switch' statement`

  - 표현식(expression)의 결과값을 이용한 조건문
  - 조건 표현식의 결과값이 어느 값(case)에 해당하는지 판별
  - break 및 default문은 [선택적]으로 사용 가능
  - break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행
  - *(참고)* 주로 특정 변수의 값에 따라 조건을 분기할 때 사용
    - 조건이 많아질 경우 if문보다 가독성이 나을 수 있음

  ```js
  switch(expression) {
    case 'first value': {
      //code
      [break]
    }
    case 'second value' : {
      // code
      [break]
    }
    [default: {
     // code
     }]
  }
  ```

  

- `if`, `else if`, `else`

  - 조건은 소괄호(condition) 안에 작성
  - 실행할 코드는 중괄호`{}` 안에 작성
  - 블록 스코프 생성

  ```js
  if (condition) {
    // code
  } else if (condition) {
    // code
  } else {
    // code
  }
  ```







#### 📝 반복문 종류와 특징

- `while`

  - 조건문이 참(ture)인 동안 반복 실행
  - 조건은 소괄호 안에 작성
  - 실행할 코드는 중괄호 안에 작성
  - 블록 스코프 생성

  ```js
  let i = 0
  
  while (i < 6) {
    console.log(i)
    i += 1
  }
  // 0, 1, 2, 3, 4, 5
  ```

- `for`

  - 세미콜론(`;`)으로 구분되는 세 부분으로 구성
  - initialization
    - 최초 반복문 진입 시 1회만 실행되는 부분
  - condition
    - 매 반복 시행 전 평가되는 부분
  - expression
    - 매 반복 시행 이후 평가되는 부분
  - 블록 스코프 생성

  ```js
  for (initialization; condition; expression) {
    // code
  }
  
  for (let i = 0; i < 6; i++) {
    console.log(i)
  }
  // 0, 1, 2, 3, 4, 5
  ```

- `fo ... in`

  - 객체의 속성(key)들을 순회할 때 사용
  - 배열도 순회 가능하지만 권장하지 않음
  - 실행할 코드는 중괄호 안에 작성
  - 블록 스코프 생성
  - 객체 순회에 적합

  ```js
  for (variable in object) {
    // code
  }
  
  const capitals = {
    korea: 'seoul',
    france: 'paris',
    USA: 'washington D.C.'
  }
  
  for (let capital in capitals) {
    console.log(capital)
  }
  // korea, france, USA
  ```

- `for ... of`

  - 반복 가능한(iterable) 객체를 순회하며 값을 꺼낼 때 사용
  - 실행할 코드는 중괄호 안에 작성
  - 블록 스코프 생성
  - 배열 순회에 적합

  ```js
  for (variable of iterables) {
    // code
  }
  
  const fruits = ['딸기', '바나나', '메론']
  
  for (let fruit of fruits) {
    fruit = ftuit + '!'
    console.log(fruit)
  }
  ```







#### 📝 함수

- `정의`

  - 함수의 이름과 함께 정의하는 방식
  - 3가지 부분으로 구성
    - 이름 (name)
    - 매개변수 (args)
    - Body (중괄호 내부)

  ```js
  function name(args) {
    // code
  }
  
  function add(num1, num2) {
    return num1 + num2
  }
  add(1, 2)
  ```

- `함수 표현식 (function expression)`

  - 함수를 표현식 내에서 정의하는 방식
    - 표현식 : 어떤 하나의 값으로 결정되는 코드의 단위
  - 함수의 이름을 생략하고 익명 함수로 정의 가능
    - 익명 함수 (anonymous function) : 이름이 없는 함수
    - 익명 함수는 함수 표현식에서만 가능
  - 3가지 부분으로 구성
    - 이름 (생략 가능)
    - 매개변수 (args)
    - body (중괄호 내부)

  ```js
  const name = function(args) {
    // code
  }
  
  const add = function(num1, num2) {
    return num1 + num2
  }
  add(1, 2)
  ```

- `기본 인자 (default arguments)`

  - 인자 작성 시 '=' 문자 뒤 기본 인자 선언 가능

  ```js
  const greeting = function (name = 'Anonymous') {
    return `hi ${name}`
  }
  greeting()
  // hi anonymous
  ```

- `매개변수와 인자의 개수 불일치 허용`

  - 매개변수보다 인자의 개수가 많을 경우

  ```js
  const noArgs = function() {
    return 0
  }
  noArgs(1, 2, 3)
  // 0
  
  const twoArgs = function(arg1, arg2) {
    return [arg1, arg2]
  }
  twoArgs(1, 2, 3)
  // [1, 2]
  ```

  - 매개변수보다 인자의 개수가 적을 경우

  ```js
  const threeArgs = function (arg1, arg2, arg3) {
    return [arg1, arg2, arg3]
  }
  threeArgs()
  // [undefined, undefined, undefined]
  threeArgs(1)
  // [1, undefined, undefined]
  threeArgs(1, 2)
  // [1, 2, undefined]
  ```

- `Rest Parameter`

  - rest parameter(...)를 사용하면 함수가 정해지지 않은 수의 매개변수를 배열로 받음
    - 만약 rest parameter로 처리한 매개변수에 인자가 넘어오지 않을 경우 빈 배열로 처리

  ```js
  const restOpr = function(arg1, arg2, ...restArgs) {
    return [arg1, arg2, restArgs]
  }
  restArgs(1, 2, 3, 4, 5)
  // [1, 2, [3, 4, 5]]
  restArgs(1, 2)
  // [1, 2, []]
  ```

- `Spread operator`

  - spread operator(...)를 사용하면 배열 인자를 전개하여 전달 가능

  ```js
  const spreadOpr = function(arg1, arg2, arg3) {
    return arg1 + arg2 + arg3
  }
  const numbers = [1, 2, 3]
  spreadOpr(...numbers)
  // 6
  ```

- `함수의 타입`

  - 선언식 함수와 표현식 함수 모두 타입은 function으로 동일

  ```js
  // 함수 표현식
  const add = function(args) { }
  
  // 함수 선언식
  function sub(args) { }
  
  console.log(typeof add)
  // function
  console.log(typeof sub)
  // function
  ```

- `호이스팅(hoistion)`

  - 함수 선언식
    - 함수 선언식으로 선언한 함수는 var로 정의한 변수처럼 hoistiong 발생
    - 함수 호출 이후에 선언해도 동작

  ```js
  add(2, 7)
  // 9
  
  function add(num1, num2) {
    return num1 + num2
  }
  ```

  - 함수 표현식
    - 함수 표현식을 var 키워드로 작성한 경우 변수가 선언 전 undefined로 초기화 되어 다른 에러가 발생

  ```js
  console.log(sub)
  // undefined
  sub(7, 2)
  // Uncaugt TypeError: sub is not a function
  
  var sub = function(num1, num2) {
    return num1 - num2
  }
  ```

- `화살표 함수 (Arrow Function)`

  - 함수를 비교적 간결하게 정의할 수 있는 문법
  - function 키워드 생략 가능
  - 함수의 매개변수가 단 하나 뿐이라면 `( )`도 생략 가능
  - 함수 body가 표현식 하나라면 `{ }`과 return도 생략 가능

  ```js
  const arrow1 = function(name) {
    return 'hello, ${name}'
  }
  
  // function 키워드 삭제
  const arrow2 = (name) => { return 'hello, ${name}' }
  
  // 매개변수가 1개일 경우에만 ( ) 생략 가능
  const arrow3 = name => { return 'hello, #{name}' }
  
  // 함수 body가 return을 포함한 표현식 1개일 경우
  // { }과 return 삭제 가능
  const arrow4 = name => `hello, ${name}`
  ```

  