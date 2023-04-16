/* 다음은 어느 자동차 회사에서 대여 중인 자동차들의 정보를 담은
CAR_RENTAL_COMPANY_CAR 테이블과 자동차 대여 기록
정보를 담은 CAR_RENTAL_COMPANY_RENTAL_HISTORY
테이블과 자동차 종류별 대여 기간 종류별 할인 정책 정보를 담은
CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블이다
CAR_RENTAL_COMPANY_CAR 테이블은 아래와 같은 구조로
되어있으며 CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS는
각각 자동차 ID, 자동차 종류, 일일 대여 요금(원), 자동차 옵션
리스트를 나타낸다. 자동차 종류는 '세단', 'SUV', '승합차', '트럭',
'리무진'이 있다. 자동차 옵션 리스트는 콤마로 구분된 키워드 리스트
(예: '열선시트, 스마트키, 주차감지센서')로 되어있으며 키워드 종류는
'주차감지센서', '스마트키', '네비게이션', '통풍시트', '열선시트',
'후방카메라', '가죽시트'가 있다
CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블은
아래와 같은 구조로 되어있으며 HISTORY_ID, CAR_ID, 
START_DATE, END_DATE는 각각 자동차 대여 기록 ID,
자동차 ID, 대여 시작일, 대여 종료일을 나타낸다
CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블은
아래와 같은 구조로 되어있으며 PLAN_ID, CAR_TYPE, 
DURATION_TYPE, DISCOUNT_RATE는 각각 요금 할인
정책 ID, 자동차 종류, 대여 기간 종류, 할인율(%)을 나타낸다
할인율이 적용되는 대여 기간 종류는 '7일 이상' (대여 기간이
7일 이상 30일 미만인 경우), '30일 이상' (대여 기간이 30일
이상 90일 미만인 경우), '90일 이상' (대여 기간이 90일 이상인
경우)이 있다. 대여기간이 7일 미만인 경우 할인정책이 없다
세 테이블에서 자동차 종류가 '세단' 또는 'SUV'인 자동차 중
2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 
30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에
대해서 자동차 ID, 자동차 종류, 대여 금액(컬럼명 : FEE) 리스트를
출력하는 SQL문을 작성하라. 결과는 대여 금액을 기준으로 
내림차순 정렬하고, 대여 금액이 같은 경우 자동차 종류를 기준으로
오름차순 정렬, 자동차 종류까지 같은 경우 자동차 ID를 기준으로
내림차순 정렬 */

SELECT A.CAR_ID, A.CAR_TYPE, ROUND(A.DAILY_FEE * 30 * (100 - C.DISCOUNT_RATE) / 100) AS FEE
FROM CAR_RENTAL_COMPANY_CAR A
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY B ON A.CAR_ID = B.CAR_ID
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN C ON A.CAR_TYPE = C.CAR_TYPE
WHERE A.CAR_ID NOT IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE > '2022-11-01' AND START_DATE < '2022-12-01' 
) AND C.DURATION_TYPE = '30일 이상'
GROUP BY A.CAR_ID
HAVING A.CAR_TYPE IN ('세단', 'SUV') AND (FEE >= 500000 AND FEE < 2000000)
ORDER BY FEE DESC, A.CAR_TYPE, A.CAR_ID DESC;