# 문자 'A'와 'B'로 이루어진 문자열 myString과 pat이 주어진다
# myString의 'A'를 'B'로 바꾼 문자열의 연속하는 부분 문자열 중
# pat이 있으면 1을, 아니면 0을 return

def solution(myString, pat):
    string = myString.replace('A', 'X').replace('B', 'A').replace('X', 'B')
    if pat in string:
        return 1
    else:
        return 0