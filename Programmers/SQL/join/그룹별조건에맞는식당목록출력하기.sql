/* 다음은 식당의 정보를 담은 REST_INFO 테이블과 식당의
리뷰 정보를 담은 REST_REVIEW 테이블이다. MEMBER_PROFILE
테이블은 다음과 같으며 MEMBER_ID, MEMBER_NAME,
TLNO, GENDER, DATE_OF_BIRTH는 회원 ID, 회원 이름,
회원 연락처, 성별, 생년월일을 의미한다.
REST_REVIEW 테이블은 다음과 같으며 REVIEW_ID, REST_ID,
MEMBER_ID, REVIEW_SCORE, REVIEW_TEXT,
REVIEW_DATE는 각각 리뷰 ID, 식당 ID, 회원 ID, 점수,
리뷰 텍스트, 리뷰 작성일을 의미한다
MEMBER_PROFILE과 REST_REVIEW 테이블에서 리뷰를 가장
많이 작성한 회원의 리뷰들을 조회하는 SQL문을 작성하라
회원 이름, 리뷰 텍스트, 리뷰 작성일이 출력되도록 하고, 결과는
리뷰 작성일을 기준으로 오름차순, 리뷰 작성일이 같다면 리뷰
텍스트를 기준으로 오름차순 정렬 */

SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE A
JOIN REST_REVIEW B ON A.MEMBER_ID = B.MEMBER_ID
WHERE A.MEMBER_ID = (
    SELECT MEMBER_ID
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    ORDER BY COUNT(*) DESC LIMIT 1
)
ORDER BY REVIEW_DATE, REVIEW_TEXT;