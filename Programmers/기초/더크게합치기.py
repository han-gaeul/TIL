# 연산 +는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값 반환
# 예) 12 + 3 = 123, 3 + 12 = 312
# 양의 정수 a와 b가 주어졌을 때, a + b와 b + a중 더 큰 값을 반환
# 단, a + b와 b + a가 같다면 a + b를 반환

def solution(a, b):
    x = str(a) + str(b)
    y = str(b) + str(a)
    if x > y:
        return int(x)
    elif x < y:
        return int(y)
    else:
        return int(x)