### `CSS`

***

##### 📝 CSS 기초

- Cascading Style Sheets

- <span style='background-color: #f1f8ff'>스타일을 지정하기 위한 언어</span>

- 예시

  ```css
  h1 {
    color: blue;
    font-size: 15px;
  }
  ```

  - `h1` 선택자(Selector)
  - `color: blue;` 선언(Declaration)
  - `font-size` 속성(Property)
  - `15px` 값(Value)

- 선택자를 통해 스타일을 지정할 HTML 요소 선택

- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행

- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미

  - 속성 (Property) : 어떤 스타일 기능을 변경할지 결정
  - 값 (Value) : 어떻게 스타일 기능을 변경할지 결정







##### 📝 CSS 정의 방법

- `인라인(inline)`

  - 해당 태그에 직접 style 속성 활용

  ```css
  <body>
  	<h1 style="color:blue; font-size: 100px;">Hello</h1>
  </body>
  ```

- `내부 참조`

  - < head > 태그 내에 < style >에 지정

  ```css
  <style>
    h1 {
      color: blue;
      font-size: 100px;
    }
  </style>
  ```

- `외부 참조`

  - 외부 CSS 파일을 < head >내 < link >를 통해 불러오기

  ```css
  <head>
  	<link rel="stylesheet" href="mystyle.css">
  </head>
  ```

  





##### 📝 CSS 기초 선택자

- `요소 선택자`
  - HTML 태그를 직접 선택
- `클래스(class) 선택자`
  - 마침표(.) 문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- `아이디(id) 선택자`
  - '#' 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용
  - 여러 번 사용해도 동작하지만 단일 id 사용을 권장

