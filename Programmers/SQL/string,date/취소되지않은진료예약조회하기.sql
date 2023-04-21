/* 다음은 환자 정보를 담은 PATIENT 테이블과 의사 정보를 담은 DOCTOR 테이블, 그리고 진료
예약목록을 담은 APPOINTMENT에 대한 테이블이다. PATIENT 테이블은 다음과 같으며 PT_NO,
PT_NAME, GEND_CD, AGE, TLNO는 각각 환자번호, 환자이름, 성별코드, 나이, 전화번호를 의미한다
DOCTOR 테이블은 다음과 같으며 DR_NAME, DR_ID, LCNS_NO, HIRE_YMD, MCDP_CD, TLNO는
각각 의사이름, 의사 ID, 면허번호, 고용일자, 진료과코드, 전화번호를 나타낸다
APPOINTMENT 테이블은 다음과 같으며 APNT_YMD, APNT_NO, PT_NO, MCDP_CD, MDDR_ID,
APNT_CNCL_YMD, APNY_CNCL_YMD는 각각 진료 예약일시, 진료예약번호, 환자번호, 진료과코드,
의사 ID, 예약취소여부, 예약취소날짜를 나타낸다
세 테이블에서 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회하는 SQL문을 작성하라
진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목이 출력되도록 하고, 결과는
진료예약일시를 기준으로 오름차순 정렬 */

SELECT APNT_NO, PT_NAME, A.PT_NO, B.MCDP_CD, DR_NAME, APNT_YMD
FROM PATIENT A
JOIN APPOINTMENT C ON A.PT_NO = C.PT_NO
JOIN DOCTOR B ON B.DR_ID = C.MDDR_ID
WHERE APNT_CNCL_YMD IS NULL AND C.MCDP_CD = 'CS' AND APNT_YMD LIKE '2022-04-13%'
ORDER BY APNT_YMD;