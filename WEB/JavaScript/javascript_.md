### `JavaScript - 변수와 식별자`

***

- 식별자(identifier)는 변수를 구분할 수 있는 변수명을 말함

- 식별자는 반드시 문자, 달러(`$`) 또는 밑줄(`_`)로 시작

- 대소문자를 구분하며 클래스명 외에는 모두 소문자로 시작

- 예약어 사용 불가능

  - 예) for, if, function 등

- 선언 (Declaration)

  - 변수를 생성하는 행위 또는 시점

  ```js
  // 선언
  let foo
  // undefined
  console.log(foo)
  ```

- 할당 (Assignment)

  - 선언된 변수에 값을 저장하는 행위 또는 시점

  ```js
  // 할당
  foo = 11
  // 11
  console.log(foo)
  ```

- 초기화(Initialzation)

  - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

  ```js
  // 선언 + 할당
  let bar = 0
  // 0
  console.log(bar)
  ```







##### 🔎 let, const

- `let`

  - 재할당 가능

  ```js
  // 1. 선언 및 초기값 할당
  let number = 10
  // 2. 재할당
  number = 10
  
  //10
  console.log(number)
  ```

  - 재선언 불가능

  ```js
  // 1. 선언 및 초기값 할당
  let number = 10
  // 2. 재선언 불가능
  let number = 50
  
  // Uncaught SyntaxError
  // : Identifier 'number' has already been declared
  ```

- `const`

  - 재할당 불가능

  ```js
  // 1. 선언 및 초기값 할당
  const number = 10
  // 2. 재할당 불가능
  number = 10
  
  // Uncaught TypeError
  // : Assignment to constant variable.
  ```

  - 재선언 불가능

  ```js
  // 1. 선언 및 초기값 할당
  const number = 10
  // 2. 재선언 불가능
  const number = 50
  
  // Uncaught SyntaxError
  // : Identifier 'number' has already been declared
  ```

- `블록 스코프 (block scope)`

  - if, for, 함수 등의 중괄호 내부를 가리킴
  - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

  ```js
  let x = 1
  
  if (x === 1) {
    let x = 2
    // 2
    console.log(x)
  }
  
  // 1
  console.log(x)
  ```

  





##### 🔎 var

- var로 선언한 변수는 재선언 및 재할당 모두 가능

  ```js
  // 1. 선언 및 초기값 할당
  var number = 10
  // 2. 재할당
  var number = 50
  
  // 50
  console.log(number)
  ```

- ES6 이전에 변수를 선언할 때 사용하던 키워드

- 호이스팅(hoisting) 되는 특성으로 예기치 못한 문제 발생 가능

  - 변수를 선언 이전에 참조할 수 있는 현상
  - 변수 선언 이전의 위치에서 접근 시 undefined를 반환
  - 자바스크립트는 모든 선언을 호이스팅 함
  - 즉, `var`, `let`, `const` 모두 호이스팅이 발생하지만 `var`는 선언과 초기화가 동시에 발생하여 일시적 사각지대가 존재하지 않음
  - ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장

  ```js
  // undefined
  console.log(username)
  var username = '홍길동'
  
  // Uncaught ReferenceError
  console.log(email)
  let email = 'honggildong@gmail.com'
  
  // Uncaught ReferenceError
  console.log(age)
  const age = 50
  ```

- 함수 스코프 (function scope)

  - 함수의 중괄호 내부를 가리킴
  - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

  ```js
  function foo() {
    var x = 5
    // 5
    console.log(x)
  }
  
  // ReferenceError: x is not defined
  console.log(x)
  ```







##### 📖 데이터 타입

- 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐
- 크게 원시 타입(Primitive type)과 참조 타입(Reference type)으로 분류됨
- 원시 타입(Primitive type)
  - 객체(object)가 아닌 기본 타입