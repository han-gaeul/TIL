/* 다음은 어느 의류 쇼핑몰에 가입한 회원 정보를 담은 USER_INFO 테이블이다
USER_INFO 테이블은 아래와 같은 구조로 되어있으며 USER_ID, GENDER,
AGE, JOINED는 각각 회원 ID, 성별, 나이, 가입일을 나타낸다
Column name / Type / Nullable
USER_ID / INTEGER / FALSE
GENDER / TINYINT(1) / TRUE
AGE / INTEGER / TRU
JOINED / DATE / FALSE
GENDER 컬럼은 비었거나 0 또는 1의 값을 가지며 0인 경우 남자를, 1인 경우는
여자를 나타낸다
USER_INFO 테이블에서 2021년에 가입한 회원 중 나이가 20세 이상 29세 이하인
회원히 몇 명인지 출력하는 SQL문을 작성하라 */

SELECT COUNT(*)
FROM USER_INFO
WHERE YEAR(JOINED) = 2021 AND 20 <= AGE AND AGE <= 29;