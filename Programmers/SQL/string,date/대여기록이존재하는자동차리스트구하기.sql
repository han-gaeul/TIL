/* 다음은 어느 자동차 대여 회사에서 대여 중인 자동차들의 정보를 담은 CAR_RENTAL_COMPANY_CAR
테이블과 자동차 대여 기록 정보를 담은 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블이다
CAR_RENTAL_COMPANY_CAR 테이블은 다음과 같은 구조로 되어있으며, CAR_ID, CAR_TYPE,
DAILY_FEE, OPTIONS는 각각 자동차 ID, 자동차 종류, 일일 대여 요금(원), 자동차 옵션 리스트를 나타낸다
자동차 종류는 '세단', 'SUV', '승합차', '트럭', '리무진'이 있다. 자동차 옵션 리스트는 콤마로 구분된 키워드
리스트(예: '열선시트', '스마트키', '주차감지센서')로 되어있으며, 키워드 종류는 '주차감지센서', '스마트키', 
'네비게이션', '통풍시트', '열선시트', '후방카메라', '가죽시트'가 있다. 
CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블은 아래와 같은 구조로 되어있으며, HISTORY_ID,
CAR_ID, START_DATE, END_DATE는 각각 자동차 대여 기록 ID, 자동차 ID, 대여 시작일, 대여 종료일을
나타낸다. 
두 테이블에서 자동차 종류가 '세단'인 자동차들 중 10월에 대여를 시작한 기록이 있는 자동차 ID 리스트를
출력하는 SQL문을 작성하라. 자동차 ID 리스트는 중복이 없어야 하며, 자동차 ID를 기준으로 내림차순 정렬 */

SELECT DISTINCT(A.CAR_ID)
FROM CAR_RENTAL_COMPANY_CAR A
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY B ON A.CAR_ID = B.CAR_ID
WHERE A.CAR_TYPE LIKE '세단' AND MONTH(START_DATE) = '10'
ORDER BY A.CAR_ID DESC;