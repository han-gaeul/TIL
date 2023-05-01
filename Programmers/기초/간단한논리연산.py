# boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때
# 다음의 식의 true/false를 반환

def solution(x1, x2, x3, x4):
    res1 = x1 or x2
    res2 = x3 or x4
    return res1 and res2