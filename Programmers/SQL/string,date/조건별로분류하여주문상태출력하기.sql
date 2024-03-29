/* 다음은 식품공장의 주문정보를 담은 FOOD_ORDER 테이블이다. FOOD_ORDER 테이블은 다음과 
같으며 ORDER_ID, PRODUCT_ID, AMOUNT, PRODUC_DATE, IN_DATE, OUT_DATE,
FACTORY_ID, WAREHOUSE_ID는 각각 주문 ID, 제품 ID, 주문양, 생산일자, 입고일자, 출고일자,
공장 ID, 창고 ID를 의미한다. 
FOOD_ORDER 테이블에서 5월 1일을 기준으로 주문 ID, 제품 ID, 출고일자, 출고여부를 조회하는 SQL문을
작성하라. 출고여부는 5월 1일까지 출고완료로, 이 후 날짜는 출고 대기로, 미정이면 출고 미정으로 출력하고
결과는 주문 ID를 기준으로 오름차순 정렬  */

SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS OUT_DATE,
    (CASE WHEN DATEDIFF(OUT_DATE, '2022-05-01') <= 0 THEN '출고완료'
        WHEN DATEDIFF(OUT_DATE, '2022-05-01') > 0 THEN '출고대기'
        ELSE '출고미정' END) AS '출고여부'
FROM FOOD_ORDER
ORDER BY ORDER_ID;