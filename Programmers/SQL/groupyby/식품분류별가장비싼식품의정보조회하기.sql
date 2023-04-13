/* 다음은 식품의 정보를 담은 FOOD_PRODUCT 테이블이다. FOOD_PRODUCT 테이블은 다음과 같으며
PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE는 식품 ID, 식품 이름,
식품코드, 식품분류, 식품 가격을 의미한다
FOOD_PRODUCT 테이블에서 식품 분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회하는
SQL문을 작성하라. 이때 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력하고 결과는 식품 가격을
기준으로 내림차순 정렬 */

SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE PRICE IN(
    SELECT MAX(PRICE)
    FROM FOOD_PRODUCT
    GROUP BY CATEGORY
) AND CATEGORY IN ('과자', '국', '김치', '식용유')
GROUP BY CATEGORY
ORDER BY MAX_PRICE DESC;