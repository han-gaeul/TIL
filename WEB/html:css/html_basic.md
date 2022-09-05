### `HTML`

***

##### ✍️ HTML 기초

- HTML이란?
  - 웹 페이지를 작성(구조화)하기 위한 언어

- Hyper Text Markup Language

  - Hyper Text : 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

  - Markup Language : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Hello, HTML</title>
  </head>
  <body>
  </body>
  </html>
  ```

  





##### ✍️ HTML 기본 구조

- `html` : 문서의 최상위(root) 요소
- `head` : 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
  - 예시
    - `titlt` : 브라우저 상단 타이틀
    - `meta` : 문서 레벨 메타데이터 요소
    - `link` : 외부 리소스 연결 요소 (CSS 파일, favicon 등)
    - `style` : CSS 직접 작성
- `body` : 문서 본문 요소
  - 실제 화면 구성과 관련된 내용

- 요소(enement)

  - <span style='background-color: #fff561'>< h1 ></span>*(여는/시작)태그* contents <span style='background-color: #fff561'>< /h1 ></span>*(닫는/종료)태그*
    - HTML의 요소는 태그와 내용(contents)로 구성
    - 태그로 내용을 감싼느 것으로 그 정보의 성격과 의미를 정의
    - 내용이 없는 태그들도 존재(닫는 태그가 없음)
      - `br`, `hr`, `img`, `input`, `link`, `meta`
  - 중첩(nested) 사용 가능
    - 중첩을 통해 하나의 문서를 구조화
    - 여는 태그와 닫는 태그의 쌍을 잘 확인 해야 함
      - 오류를 반환하는 것이 아닌 레이아웃이 깨진 상태로 출력되기 때문에 디버깅이 힘들어질 수 있음
  - 인라인 / 블록 요소
    - 인라인 요소는 글자처럼 취급
    - 블록 요소는 한 줄 모두 사용
  - 텍스트 요소

  | 태그                                 | 설명                                                         |
  | ------------------------------------ | ------------------------------------------------------------ |
  | < a >< /a >                          | href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성     |
  | < b >< /b ><br>< strong >< /strong > | 굵은 글씨 요소<br>중요한 강조하고자 하는 요소 (보통 굵은 글씨로 표현) |
  | < i >< /i ><br>< em >< /em >         | 기울임 글씨 요소<br>중요한 강조하고자 하는 요소 (보통 기울임 글씨로 표현) |
  | < br >                               | 텍스트 내에 줄 바꿈 생성                                     |
  | < img >                              | src 속성을 활용하여 이미지 표현,<br>alt 속성을 활용하여 대체 텍스트 |
  | < span >< /span >                    | 의미 없는 인라인 컨테이너                                    |

  - 그룹 컨텐츠

  | 태그                           | 설명                                                         |
  | ------------------------------ | ------------------------------------------------------------ |
  | < p >< /p >                    | 하나의 문단 (paragraph)                                      |
  | < hr >                         | 문단 레벨 요소에서의 주제의 분리를 의미하며<br>수평선으로 표현됨 (A Horizontal Rule) |
  | < ol >< /ol ><br>< ul >< /ul > | 순서가 있는 리스트 (ordered) <br/>순서가 없는 리스트 (unordered) |
  | < pre >< /pre >                | HTML에 작성한 내용을 그대로 표현<br>보통 고정폭 글꼴이 사용되고 공백문자를 유지 |
  | < blockquote >< /blockquote >  | 텍스트가 긴 인용문<br/>주로 들여쓰기를 한 것으로 표현됨      |
  | < div >< /div >                | 의미 없는 블록 레벨 컨테이너                                 |

- 속성(attribute)

  - <a <span style='background-color: #fff561'>href</span>*(속성명)*="<span style='background-color: #f1f8ff'>https://google.com</span>*(속성값)*"></a>

    - 속성 지정 스타일 가이드 ➡︎ 공백X, 쌍타옴표(" ") 사용

  - 속성을 통해 태그의 부가적인 정보를 설정할 수 있음

  - 요소는 속성을 가질 수 있으며 경로나 크기와 같은 추가적인 정보를 제공

  - 요소의 시작 태그에 작성하며 보통 이름과 같이 하나의 쌍으로 존재

  - 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음

    💡 HTML Gobal Attribute

    - 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성
      - `id` : 문서 전체에서 유일한 고유 식별자 지정
      - `class` : 공백으로 구분된 해당 요소의 클래스의 목록(CSS, JS에서 요소를 선택하거나 접근)
      - `data-*` : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
      - `style` : inline 스타일
      - `title` : 요소에 대한 추가 정보 지정
      - `tabindex` : 요소의 탭 순서

- HTML 코드 예시

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>
  <!-- 주석 -->
  <h1>첫번째 HRML</h1>
  <p>본문</p>
  <span>인라인요소</span>
  <a href="https://www.github.com">깃허브</a>
</body>
</html>
```

