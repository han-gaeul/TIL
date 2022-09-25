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







#### 🔎 let, const

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

  





#### 🔎 var

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







#### 📖 데이터 타입

- 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐

- 크게 원시 타입(Primitive type)과 참조 타입(Reference type)으로 분류됨

- `원시 타입(Primitive type)`
  
  - 객체(object)가 아닌 기본 타입
  - 변수에 해당 타입의 값이 담김
  - 다른 변수에 복사할 때 실제 값이 복사됨
  
  ```js
  // message 선언 및 할당
  let message = '안녕하세요'
  
  // greeting에 message 복사
  let greeting = message
  // '안녕하세요' 출력
  console.log(greeting)
  
  // message 재할당
  message = 'hello, world'
  // '안녕하세요' 출력
  console.log(greeting)
  ```
  
  > 원시 타입은 실제 해당 타입의 값을 변수에 저장
  
- `참조 타입 (Reference type)`
  
  - 객체 타입의 자료형
  - 변수에 해당 객체의 참조 값이 담김
  - 다른 변수에 복사할 때 참조 값이 복사됨
  
  ```js
  // message 선언 및 할당
  const message = ['안녕하세요']
  
  // greeting에 message 복사
  const greeting = message
  // '안녕하세요' 출력
  console.log(greeting)
  
  // message 재할당
  message[0] = 'hello, world'
  // 'hello, world' 출력
  console.log(greeting)
  ```
  
  > 참조 타입은 해당 객체를 참조할 수 있는 참조 값을 저장

- `숫자 (Number) 타입`

  - 정수, 실수 구분 없는 하나의 숫자 타입
  - 부동소수점 형식을 따름
  - *(참고)* NaN (Not-A-Number)
    - 계산 불가능한 경우 반환되는 값
    - ex) 'Angel' / 1004 ➡︎ NaN

  ```js
  const a = 13
  const b = -5
  const c = 3.14
  const d = 2.998e8 // 거듭제곱
  const e = Infinity // 양의 무한대
  const f = -Infinity // 음의 무한대
  const g = NaN // 산술 연산 불가
  ```

- `문자열 (String) 타입`

  - 텍스트 데이터를 나타내는 타입
  - 16비트 유니코드 문자의 집합
  - 작은따옴표 또는 큰따옴표 모두 가능
  - 템플릿 리터럴(Template Literal)
    - ES6부터 지원
    - 따옴표 대신 backtick(`)으로 표현
    - ${ expression } 형태로 표현식 삽입 가능

  ```js
  const firstName = 'Hong'
  const lastName = 'gildong'
  const fullName = `${firstName} ${lastName}`
  
  console.log(fullName)
  // Hong gildong
  ```

- `null`

  - 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입

  - *(참고)* null 타입과 typeof 연산자

    - typeof 연산자 : 자료형 평가를 위한 연산자

    - null 타입은 ECMA 명세의 원시 타입의 정의에 따라 원시 타입에 속하지만,

      typeof 연산자의 결과는 객체로 표현됨

  ```js
  let firstName = null
  console.log(firstName)
  // null
  
  typeof null
  // object
  ```

- `Boolean 타입`

  - 논리적 참 또는 거짓을 나타내는 타입
  - true 또는 false로 표현
  - 조건문 또는 반복문에서 유용하게 사용
    - *(참고)* 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 자동 형변환 규칙에 따라 true 또는 false로 변환됨

  ```js
  let isAmin = true
  console.log(isAdmin)
  // true
  
  isAdmin = false
  console.log(isAdmin)
  // false
  ```

  - *(참고)* ToBoolean Conversions(자동 형변환) 정리

  | 데이터 타입 | 거짓       | 참               |
  | ----------- | ---------- | ---------------- |
  | Undefined   | 항상 거짓  | X                |
  | Null        | 항상 거짓  | X                |
  | Number      | 0, -0, NaN | 나머지 모든 경우 |
  | String      | 빈 문자열  | 나머지 모든 경우 |
  | Object      | X          | 항상 참          |







#### 📖 연산자

- `할당 연산자`

  - 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
  - 다양한 연산에 대한 단축 연산자 지원
  - *(참고)* Increment 및 Decrement 연산자
    - Increment(++) : 피연산자의 값을 1 증가시키는 연산자
    - Decrement(--) : 피연산자의 값을 1 감소시키는 연산자

  ```js
  let x = 0
  
  x += 10
  console.log(x) // 10
  
  x -= 3
  console.log(x) // 7
  
  x *= 10
  console.log(x) // 70
  
  x /= 10
  console.log(x) // 7
  
  x++ // += 연산자와 동일
  console.log(x) // 8
  
  x-- // -= 연산자와 동일
  console.log(x) // 7
  ```

- `비교 연산자`

  - 피연산자를 비교하고 결과값을 boolean으로 반환하는 연산자
  - 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교
    - 예) 알파벳끼리 비교할 경우
      - 알파벳 순서상 후순위가 더 큼
      - 소문자가 대문자보다 더 큼

  ```js
  const numOne = 1
  const numTwo = 100
  console.log(numOne < numTwo)
  // ture
  
  const charOne = 'a'
  const charTwo = 'z'
  console.log(charOne > charTwo)
  // false
  ```

- `동등 비교 연산자 (==)`

  - 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
  - 비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
  - 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
  - 예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음

  ```js
  const a = 1004
  const b = '1004'
  console.log(a == b)
  // true
  
  const c = 1
  const d = true
  console.log(c == d)
  // true
  
  //자동 타입 변환 예시
  console.log(a + b) // 10041004
  console.log(c + d) // 2
  ```

- `일치 비교 연산자 (===)`

  - 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
  - 두 비교 대상의 타입과 값이 모두 같은지 비교하기 때문에 암묵적 타입 변환이 발생하지 않음

  ```js
  const a = 1004
  const b = '1004'
  console.log(a === b)
  // false
  
  const c = 1
  const d = true
  console.log(c == d)
  // false
  ```

- `논리 연산자`

  - 세 가지 논리 연산자로 구성
    - and 연산은 '&&' 연산자를 이용
    - or 연산은 '||' 연산자를 이용
    - not 연산은 '!' 연산자를 이용
  - 단축 평가 지원
    - 예) false && ture ➡︎ false
    - 예) ture || false ➡︎ ture

  ```js
  // and 연산
  console.log(ture && false) // false
  console.log(true && true) // true
  console.log(1 && 0) // 0
  console.log(4 && 7) // 7
  console.log('' && 5) // ''
  
  // or 연산
  console.log(true || false) // true
  console.log(false || false) // false
  console.log(1 || 0) // 1
  console.log(4 || 7) // 4
  console.log('' || 5) // 5
  
  // not 연산
  console.log(!true) // false
  console.log(!'hello') // false
  ```

- `삼항 연산자`

  - 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
  - 가장 왼쪽의 조건식이 참이면 콜론(:) 앞의 값을 사용하고 그렇지 않으면 콜론(:) 뒤의 값을 사용
  - 삼항 연산자의 결과 값이기 때문에 변수에 할당 가능

  ```js
  console.log(true ? 1 : 2) // 1
  console.log(false ? 1 : 2) // 2
  
  const result = Math.PI > 4 ? 'Yes' : 'No'
  console.log(result) // No
  ```

  