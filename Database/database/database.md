### `Database`

***

- 데이터베이스는 <span style='color:#2D3748; background-color:#fff5b1'>체계화된 데이터</span>의 모임
- <span style='color:#2D3748; background-color:#fff5b1'>몇 개의 자료 파일을 조직적으로 통합</span>하여 <span style='color:#2D3748; background-color:#fff5b1'>자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체</span>



👩🏻‍💻 데이터베이스로 얻는 장점들

- 데이터 중복 최소화
- 데이터 무결성(정확한 정보를 보장)
- 데이터 일관성
- 데이터 독립성(물리적/논리적)
- 데이터 표준화
- 데이터 보안 유지







#### 📋 RDB

- `관계형 데이터베이스 (RDB, Relational Database)`

  - 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형
  - 키(Key)와 값(value)들의 간단한 관계(relation)를 표(table) 형태로 정리한 데이터베이스

  | 고유 번호 | 이름   | 주소 | 나이 |
  | --------- | ------ | ---- | ---- |
  | 1         | 홍길동 | 제주 | 20   |
  | 2         | 김철수 | 서울 | 30   |
  | 3         | 이영희 | 부산 | 40   |

- `스키마(schema)`

  - 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 <span style='color:#2D3748; background-color:#fff5b1'>명세를 기술</span>한 것

  | column  | datatype |
  | ------- | -------- |
  | id      | INT      |
  | name    | TEXT     |
  | Address | TEXT     |
  | Age     | INT      |

- `테이블(table)`

  - 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합

  <img src="/Users/goobano/Desktop/schema.png" style="zoom:50%;" />

- `열(column)`

  - 아래의 예시에서는 name이란 필드에 고객의 이름(TEXT) 정보 저장

  