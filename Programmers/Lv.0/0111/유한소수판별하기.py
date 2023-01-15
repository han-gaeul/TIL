# 소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 한다
# 분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 한다
# 유한소수가 되기 위한 분수의 조건은 다음과 같다
# 기약분수로 나타내었을 때 분모의 소인수가 2와 5만 존재해야 한다
# 두 정수 a와 b가 매개변수로 주어질 때 a/b 가
# 유한소수이면 1을, 무한소수라면 2를 return

def solution(a, b):
    # 기약 분수로 변환
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    g = gcd(a, b)
    a //= g
    b //= g

    # b의 소인수 체크
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5

    # b가 1일 경우 유한소수, 그렇지 않으면 무한소수
    if b == 1:
        return 1
    else:
        return 2


import math

def solution(a, b):
    # 기약 분수로 변환
    g = math.gcd(a, b)
    a //= g
    b //= g

    # b의 소인수 체크
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5

    # b가 1일 경우 유한소수, 그렇지 않으면 무한소수
    if b == 1:
        return 1
    else:
        return 2