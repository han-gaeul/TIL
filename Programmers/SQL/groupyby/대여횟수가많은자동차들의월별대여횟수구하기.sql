-- 다음은 어느 자동차 대여 회사의 자동차 대여 기록 정보를 담은
-- CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블이다
-- CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블은 아래와 같은 구조로 되어있으며
-- HISTORY_ID, CAR_ID, START_DATE, END_DATE는 각각 자동차 대여 기록 ID, 자동차 ID,
-- 대여 시작일, 대여 종료일을 나타낸다
-- Column name / Type / Nullable
-- HISTORY_ID / INTEGER / FALSE
-- CAR_ID / INTEGER / FASLE
-- START_DATE / DATE / FALSE
-- END_DATE / DATE / FALSE
-- 테이블에서 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인
-- 자동차들에 대해서 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수(컬럼명: RECORDS) 리스트를
-- 출력하는 SQL문을 작성하라. 결과는 월을 기준으로 오름차순 정렬하고, 월이 같다면 자동차 ID를
-- 기준으로 내림차순 정렬. 특정 월의 총 대여 횟수가 0인 경우에는 결과에서 제외

SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(CAR_ID) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE '2022-08-01' <= START_DATE AND START_DATE <= '2022-10-31'
    GROUP BY CAR_ID
    HAVING COUNT(*) >= 5
) AND '2022-08-01' <= START_DATE AND START_DATE <= '2022-10-31'
GROUP BY MONTH, CAR_ID
ORDER BY MONTH, CAR_ID DESC;