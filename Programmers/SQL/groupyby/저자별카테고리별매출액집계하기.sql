/* 다음은 어느 한 서점에서 판매중인 도서들의 정보(BOOK), 저자 정보(AUTHOR) 테이블이다
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
BOOK_SALES 테이블은 각 도서의 날짜별 판매량 정보를 담은 테이블로 아래와 같은 구조로 되어있다
Column name / Type / Nullable / Description
BOOK_ID / INTEGER / FALSE / 도서 ID
SALES_DATE / DATE / FALSE / 판매일
SALES / INTEGER / FALSE / 판매량
2022년 1월의 도서 판매 데이터를 기준으로 저자별, 카테고리별 매출액(TOTAL_SALES = 판매량 *
판매가)을 구하여, 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 
매출액(SALES) 리스트를 출력하는 SQL문을 작성하라. 결과는 저자 ID를 오름차순으로, 저자 ID가
같다면 카테고리를 내림차순 정렬 */

SELECT B.AUTHOR_ID, B.AUTHOR_NAME, A.CATEGORY, SUM(C.SALES * A.PRICE) AS TOTAL_SALES
FROM BOOK A
JOIN AUTHOR B ON A.AUTHOR_ID = B.AUTHOR_ID
JOIN BOOK_SALES C ON A.BOOK_ID = C.BOOK_ID
WHERE DATE_FORMAT(C.SALES_DATE, '%Y-%m') = '2022-01'
GROUP BY A.CATEGORY, A.AUTHOR_ID
ORDER BY A.AUTHOR_ID, A.CATEGORY DESC;