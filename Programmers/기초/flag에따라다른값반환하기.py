# 두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때
# flag가 true면 a + b를, false는 a - b를 반환

def solution(a, b, flag):
    if flag:
        return a + b
    else:
        return a - b