/* 다음은 종합병원의 진료 예약정보를 담은 APPOINTMENT
테이블이다. APPOINTMENT 테이블은 다음과 같으며, APNT_YMD,
APNT_NO, PT_NO, MCDP_CD, MDDR_ID, APNT_CNCL_YN,
APNT_CNCL_YMD는 각각 진료예약일시, 진료예약번호,
환자번호, 진료과코드, 의사 ID, 예약취소여부, 예약취소날짜를
나타낸다
Column name / Type / Nullable
APNT_YMD / TIMESTAMP / FALSE
APNT_NO / NUMBER(5) / FALSE
PT_NO / VARCHAR(10) / FALSE
MCDP_CD / VARCHAR(6) / FALSE
MDDR_ID / VARCHAR(10) / FALSE
APNT_CNCL_YN / VARCHAR(1) / TRUE
APNT_CNCL_YMD / DATE / TRUE
APPOINTMENT 테이블에서 2022년 5월에 예약한 환자 수를 
진료과코드 별로 조회하는 SQL문을 작성하라. 이때, 컬럼명은
'진료과 코드', '5월예약건수'로 지정하고 결과는 진료과별
예약한 환자 수를 기준으로 오름차순 정렬한다. 예약한 환자 수가
같다면 진료과 코드를 기준으로 오름차순 정렬 */

-- MySQL
SELECT MCDP_CD AS '진료과코드', COUNT(PT_NO) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD
ORDER BY COUNT(PT_NO), MCDP_CD;

-- Oracle
SELECT MCDP_CD AS '진료과코드', COUNT(PT_NO) AS '5월예약건수'
FROM APPOINTMENT
WHERE TO_CHAR(APNT_YMD, 'mm') = '05'
GROUP BY MCDP_CD
ORDER BY COUNT(PT_NO), MCDP_CD;