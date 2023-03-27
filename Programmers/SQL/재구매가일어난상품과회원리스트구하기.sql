/* 다음은 어느 의류 쇼핑몰의 온라인 상품 판매 정보를 담은 ONLINE_SALE 테이블이다
ONLINE_SALE 테이블은 아래와 같은 구조로 되어있으며 ONLINE_SALE_ID, USER_ID,
PRODUCT_ID, SALES_AMOUNT, SALES_DATE는 각각 온라인 상품 판매 ID, 회원 ID,
상품 ID, 판매량, 판매일을 나타낸다
Column name / Type/ Nullable
ONLINE_SALE_ID / INTEGER / FALSE
USER_ID / INTEGER / FASLE
PRODUCT_ID / INTEGER / FASLE
SALES_AMOUNT / INTEGER / FASLE
SALES_DATE / DATE / FALSE
동일한 날짜, 회원 ID, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재한다
ONLINE_SALE 테이블에서 동일한 회원이 동일한 상품을 재구매한 데이터를 구하여, 재구매한
회원 ID와 재구매한 상품 ID를 출력하는 SQL문을 작성하라. 결과는 회원 ID를 기준으로 오름차순
정렬하고 회원 ID가 같다면 상품 ID를 기준으로 내림차순 정렬 */

SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING count(*) >= 2
ORDER BY USER_ID, PRODUCT_ID DESC;