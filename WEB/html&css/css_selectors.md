### `CSS Selectors`

***

##### 📌 선택자(Selector) 유형

- 기본 선택자 
  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자
- 결합자(Combinators)
  - 자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자
- 의사 클래스/요소(Pseudo Class)
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자





##### 📌 CSS 선택자 정리

- 요소 선택자
  - HTML 태그를 직접 선택
- 클래스(class) 선택자
  - 마침표(`.`) 문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 아이디(id) 선택자
  - `#` 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용
  - 여러 번 사용해도 동작하지만 단일 id를 사용하는 것을 권장





##### 📌 CSS 적용 우선순위(cascading order)

1. 중요도 (Importance) : 사용시 주의
   - `!important`
2. 우선 순위 (Specificity)
   - 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
3. CSS 파일 로딩 순서







##### 📌 CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속함
  - 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있음
  - 상속 되는 것 예시
    - text 관련 요소(font, color, text-align), opacity, visibility 등
  - 상속 되지 않는 것 예시
    - Box model 관련 요소(width, height, margin, padding, border, box-sizing, display), position 관련 요소(position, top/right/bottom/left- z-index) 등



