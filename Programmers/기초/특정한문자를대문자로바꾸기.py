# 영소문자로 이루어진 문자열 my_string과 영소문자 1글자로
# 이루어진 문자열 alp가 매개변수로 주어질 때
# my_string에서 alp에 해당하는 모든 글자를 대문자로 바꾼
# 문자열을 return

def solution(my_string, alp):
    res = ''
    for i in my_string:
        if i == alp:
            res += i.upper()
        else:
            res += i
    return res