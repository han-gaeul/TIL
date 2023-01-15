# 머쓱이는 프로그래머스에 로그인하려고 한다
# 머쓱이가 입력한 아이디와 패스워드가 담긴 배열 id_pw와
# 회원들의 정보가 담긴 2차원 배열 db가 주어질 때
# 다음과 같이 로그인 성공, 실패에 따른 메시지를 return
# 아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 login return
# 로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 fail,
# 아이디는 일치하지만 비밀번호가 일치하는 회원이 없다면 wrong pw return


# for문
def solution(id_pw, db):
    for i in db:
        # 아이디 확인
        if id_pw[0] in i:
            # 비밀번호 확인
            if id_pw[1] == i[1]:
                return 'login'
            else:
                return 'wrong pw'
    return 'fail'


# 딕셔너리
def solution(id_pw, db):
    # 아이디를 key값으로, 비밀번호를 value값으로 딕셔너리 저장
    db_dict = {i[0]: i[1] for i in db}
    # 아이디가 있으면
    if id_pw[0] in db_dict:
        if id_pw[1] == db_dict[id_pw[0]]:
            return 'login'
        else:
            return 'wrong pw'
    else:
        return 'fail'