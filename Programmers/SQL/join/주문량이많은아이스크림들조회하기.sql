/* 다음은 아이스크림 가게의 상반기 주문 정보를 담은 FIRST_HALF
테이블과 7월의 아이스크림 주문 정보를 담은 JULY 테이블이다.
FIRST_HALF 테이블 구조는 다음과 같으며 SHIPMENT_ID,
FLAVOR, TOTAL_ORDER는 각각 아이스크림 공장에서 아이스크림
가게까지의 출하 번호, 아이스크림 맛, 상반기 아이스크림 총주문량을
나타낸다 FIRST_HALF 테이블의 기본키는 FLAVOR이다.
FIRST_HALF 테이블의 SHIPMENT_ID는 JULY 테이블의
SHIPMENT_ID의 외래 키이다
JULY 테이블 구조는 다음과 같으며 SHIPMENT_ID, FLAVOR,
TOTAL_ORDER는 각각 아이스크림 공장에서 아이스크림 가게까지의
출하 번호, 아이스크림 맛, 7월 아이스크림 총주문량을 나타낸다
JULY 테이블의 기본 키는 SHIPMENT_ID이다. JULY 테이블의
FLAVOR는 FIRST_HALF 테이블의 FLAVOR 외래 키이다.
7월에는 아이스크림 주문량이 많아 같은 아이스크림에 대하여
서로 다른 두 공장에서 아이스크림 가게로 출하를 진행하는 경우가
있다. 이 경우 같은 맛의 아이스크림이라도 다른 출하 번호를
가지게 된다. 
7월 아이스크림 총 주문량과 상반기 아이스크림 총 주문량을 더한
값이 큰 순서대로 상위 3개의 맛을 조회하는 SQL문을 작성하라 */

SELECT A.FLAVOR
FROM FIRST_HALF A
JOIN (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
    FROM JULY
    GROUP BY FLAVOR
) B ON A.FLAVOR = B.FLAVOR
ORDER BY (A.TOTAL_ORDER + B.TOTAL_ORDER) DESC LIMIT 3;