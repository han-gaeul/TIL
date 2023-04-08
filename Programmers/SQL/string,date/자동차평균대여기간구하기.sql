/* 다음은 어느 자동차 대여 회사의 자동차 대여 기록 정보를 담은
CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블이다.
이 테이블은 다음과 같은 구조로 되어있으며, HISTORY_ID, 
CAR_ID, START_DATE, END_DATE는 각각 자동차 대여 기록 ID,
자동차 ID, 대여 시작일, 대여 종료일을 나타낸다
이 테이블에서 평균 대여 기간이 7일 이상인 자동차들의 자동차 ID와
평균 대여 기간(컬럼명 : AVERAGE_DURATION) 리스트를 출력하는
SQL문을 작성하라. 평균 대여 기간은 소수점 두번째 자리에서
반올림하고, 결과는 평균 대여 기간을 기준으로 내림차순 정렬
평균 대여 기간이 같으면 자동차 ID를 기준으로 내림차순 정렬 */

SELECT CAR_ID, ROUND(AVG(DATEDIFF(END_DATE, START_DATE) + 1), 1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC;