/* 다음은 어느 한 서점에서 판매중인 도서들의 도서 정보(BOOK), 저자 정보(AUTHOR) 테이블이다
BOOK 테이블은 각 도서의 정보를 담은 테이블로 아래와 같은 구조로 되어있다
Column name / Type / Nullable / Description
BOOK_ID / INTEGER / FALSE / 도서 ID
CATEGORY / VARCHAR(N) / FALSE / 카테고리(경제, 인문, 소설, 생활, 기술)
AUTHOR_ID / INTEGER / FALSE / 저자 ID
PRICE / INTEGER / FALSE / 판매가(원)
PUBLISHED_DATE / DATE / FALSE / 출판일
AUTHOR 테이블은 도서의 저자의 정보를 담은 테이블로 아래와 같은 구조로 되어있다
Column name / Type / Nullable / Description
AUTHOR_ID / INTEGER / FALSE / 저자 ID
AUTHOR_NAME / VARCHAR(N) / FALSE / 저자명
'경제' 카테고리에 속하는 도서들의 도서 ID, 저자명, 출판일 리스트를 출력하는 SQL문을 작성하라
결과는 출판일을 기준으로 오름차순 정렬 */

SELECT A.BOOK_ID, B.AUTHOR_NAME, DATE_FORMAT(A.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK A
JOIN AUTHOR B ON A.AUTHOR_ID = B.AUTHOR_ID
WHERE A.CATEGORY LIKE '경제'
ORDER BY PUBLISHED_DATE;