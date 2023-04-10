/* 다음은 중고 거래 게시판 정보를 담은 USED_GOODS_BOARD
테이블과 중고 거래 게시판 첨부파일 정보를 담은 USED_GOODS_FILE
테이블이다. USED_GOODS_BOARD 테이블은 다음과 같으며
BOARD_ID, WRITER_ID, TITLE, CONTENTS, PRICE,
CREATED_DATE, STATUS, VIEWS는 게시글 ID, 작성자 ID,
게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수를 의미한다
USED_GOODS_USER 테이블은 다음과 같으며 USER_ID,
NICKNAME, CITY, STREET_ADDRESS1, STREET_ADDRESS2,
TLNO는 각각 회원 ID, 닉네임, 시, 도로명 주소, 상세 주소,
전화번호를 의미한다.
USED_GOODS_BOARD와 UESD_GOODS_USER 테이블에서
중고 거래 게시물을 3건 이상 등록한 사용자의 사용자 ID, 닉네임,
전체주소, 전화번호를 조회하는 SQL문을 작성하라. 이때, 전체
주소는 시, 도로명, 주소, 상세 주소가 함께 출력되도록 하고,
전화번호의 경우 xxx-xxxx-xxxx 같은 형태로 하이픈 문자열을
삽입하여 출력. 결과는 회원 ID를 기준으로 내림차순 정렬 */

SELECT B.USER_ID, B.NICKNAME,
    CONCAT(B.CITY, ' ', B.STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS '전체주소',
    CONCAT(SUBSTR(B.TLNO, 1, 3), '-', SUBSTR(B.TLNO, 4, 4), '-', SUBSTR(B.TLNO, 8)) AS '전화번호'
FROM USED_GOODS_BOARD A
JOIN USED_GOODS_USER B ON A.WRITER_ID = B.USER_ID
GROUP BY A.WRITER_ID
HAVING COUNT(A.WRITER_ID) >= 3
ORDER BY B.USER_ID DESC;