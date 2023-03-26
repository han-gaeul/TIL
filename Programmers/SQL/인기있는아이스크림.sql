/* FIRST_HALF 테이블은 아이스크림 가게의 상반기 주문 정보를 담은 테이블이다
FIRST_HALF 테이블 구조는 다음과 같으며, SHIPMENT_ID, FLAVOR, TOTAL_ORDER는
각각 아이스크림 공장에서 아이스크림 가게까지의 출하 번호, 아이스크림 맛, 상반기
아이스크림 총 주문량을 나타낸다
NAME / TYPE / NULLABLE
SHIPMENT_ID / INT(N) / FALSE
FLAVOR / VARCHAR(N) / FALSE
TOTAL_ORDER / INT(N) / FALSE
상반기에 판매된 아이스크림의 맛을 총 주문량을 기준으로 내림차순 정렬하고
총 주문량이 같다면 출하 번호를 기준으로 오름차순 정렬하여 조회하는 SQL문을 작성하라 */

SELECT FLAVOR
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID