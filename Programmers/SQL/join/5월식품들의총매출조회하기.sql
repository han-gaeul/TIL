/* 다음은 식품의 정보를 담은 FOOD_PRODUCT 테이블과
식품의 주문 정보를 담은 FOOD_ORDER 테이블이다. 
FOOD_PRODUCT 테이블은 다음과 같으며 PRODUCT_ID,
PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE는
식품 ID, 식품 이름, 식품코드, 식품분류, 식품 가격을 의미한다
FOOD_ORDER 테이블은 다음과 같으며 ORDER_ID, PRODUCT_ID,
AMOUNT, PRODUCE_DATE, IN_DATE, OUT_DATE,
FACTORY_ID, WAREHOUSE_ID는 각각 주문 ID, 제품 ID,
주문량, 생산일자, 입고일자, 출고일자, 공장 ID, 창고 ID를 의미한다
두 테이블에서 생산일자가 2022년 5월인 식품들의 식품 ID,
식품 이름, 총매출을 조회하는 SQL문을 작성하라. 이때 결과는
총매출을 기준으로 내림차순 정렬하고 총매출이 같다면 식품 ID를
기준으로 오름차순 정렬 */

SELECT A.PRODUCT_ID, A.PRODUCT_NAME, SUM(PRICE * AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT A
JOIN FOOD_ORDER B ON A.PRODUCT_ID = B.PRODUCT_ID
WHERE PRODUCE_DATE LIKE '2022-05%'
GROUP BY A.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, A.PRODUCT_ID;