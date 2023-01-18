# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한
# 모든 정수의 합을 return
# 예를 들어 a = 3, b = 5인 경우 3 + 4 + 5 = 12 이므로 12 return

def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))