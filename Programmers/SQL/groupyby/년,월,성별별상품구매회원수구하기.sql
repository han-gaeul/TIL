/* 다음은 어느 의류 쇼핑몰에 가입한 회원 정보를 담은 USER_INFO 테이블과 온라인 상품 판매
정보를 담은 ONLINE_SALE 테이블이다. USER_INFO 테이블은 아래와 같은 구조로 되어있으며
USER_ID, GENDER, AGE, JOINED는 각각 회원 ID, 성별, 나이, 가입일을 나타낸다
GENDER 컬럼은 비어있거나 0 또는 1의 값을 가지며 0인 경우 남자를, 1인 경우 여자를 나타낸다
ONLINE_SALE 테이블은 아래와 같은 구조로 되어있으며 ONLINE_SALE_ID, USER_ID,
PRODUCT_ID, SALES_AMOUNT, SALES_DATE는 각각 온라인 상품 판매 ID, 회원 ID,
상품 ID, 판매량, 판매일을 나타낸다. 동일한 날짜, 회원 ID, 상품 ID 조합에 대해서는 하나의 판매
데이터만 존재한다.
USER_INFO 테이블과 ONLINE_SALE 테이블에서 년, 월, 성별별로 상품을 구매한 회원수를
집계하는 SQL문을 작성하라. 결과는 년, 월, 성별을 기준으로 오름차순 정렬. 이때, 성별 정보가
없는 경우 결과에서 제외 */

SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, GENDER, COUNT(DISTINCT A.USER_ID) AS USERS
FROM USER_INFO A
JOIN ONLINE_SALE B ON A.USER_ID = B.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE), GENDER
ORDER BY YEAR(SALES_DATE), MONTH(SALES_DATE), GENDER;