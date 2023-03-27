/* 다음은 아이스크림 가게의 상반기 주문 정보를 담은 FIRST_HALF 테이블과
아이스크림 성분에 대한 정보를 담은 ICECREAM_INFO 테이블이다
FIRST_HALF 테이블 구조는 다음과 같으며, SHIPMENT_ID, FLAVOR,
TOTAL_ORDER는 각각 아이스크림 공장에서 아이스크림 가게까지의 출하 번호,
아이스크림 맛, 상반기 아이스크림 총 주문량을 나타낸다. FIRST_HALF 테이블의
기본 키는 FLAVRO이다
NAME / TYPE / NULLABLE
SHIPMENT_ID / INT(N) / FALSE
FLAVOR / VARCHAR(N) / FALSE
TOTAL_ORDER / INT(N) / FALSE
ICECREAM_INFO 테이블 구조는 다음과 같으며 FLAVOR, INGREDITENT_TYPE은
각각 아이스크림 맛, 아이스크림의 성분 타입을 나타낸다. INGREDITENT_TYPE에는
아이스크림의 주성분이 설탕이면 sugar_based라고 입력되고, 아이스크림의 주 성분이
과일이면 fruit_based라고 입력 된다. ICECREAM_INFO의 기본 키는 FLAVOR이다
ICECREAM_INFO 테이블의 FLAVOR는 FIRST_HALF 테이블의 FLAVOR의 외래 키이다
NAME / TYPE / NULLABLE
FLAVOR / VARCHAR(N) / FALSE
INGREDIENT_TYPE / VARCHAR(N) / FALSE
상반기 아이스크림 총 주문량이 3,000보다 높으면서 아이스크림의 주 성분이 과일인
아이스크림의 맛을 총 주문량이 큰 순서대로 조회하는 SQL문을 작성하라 */

SELECT A.FLAVOR
FROM FIRST_HALF A
JOIN ICECREAM_INFO B ON A.FLAVOR = B.FLAVOR
WHERE A.TOTAL_ORDER > 3000 AND B.INGREDIENT_TYPE = 'fruit_based'
ORDER BY A.TOTAL_ORDER DESC;