/* 다음은 종합병원에 등록된 환자정보를 담은 PATIENT 테이블이다
PATIENT 테이블은 다음과 같으며 PT_NO, PT_NAME, GEND_CD,
AGE, TLNO는 각각 환자 번호, 환자 이름, 성별코드, 나이, 전화번호를 의미한다
Column name / Type / Nullable
PT_NO / VARCHAR(10) / FALSE
PT_NAME / VARCHAR(20) / FALSE
GEND_CD / VARCHAR(1) /FALSE
AGE / INTEGER / FALSE
TLNO / VARCHAR(50) / TRUE
PATIENT 테이블에서 12세 이하인 여자 환자의 환자 이름, 환자 번호, 성별 코드,
나이, 전화번호를 조회하는 SQL문을 작성하라
이때 전화번호가 없는 경우, 'NONE'으로 출력하고 결과는 나이를 기준으로 내림차순
정렬한다. 나이가 같다면 환자이름을 기준으로 오름차순 정렬 */

SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO
FROM PATIENT
WHERE AGE <= 12 AND GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME;