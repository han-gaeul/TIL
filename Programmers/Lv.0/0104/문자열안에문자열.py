# 문자열 str1, str2가 매개변수로 주어진다
# str1 안에 str2가 있다면 1을, 없다면 2를 return

def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2

def solution(str1, str2):
    return 1 if str2 in str1 else 2

# [ 조건 만족 시 출력값 if 조건 else 조건 불만족 시 출력 값 for i in data] 
