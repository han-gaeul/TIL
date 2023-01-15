# i 팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미한다
# 예를 들어 5! = 5 * 4 * 3 * 2 * 1 = 120
# 정수 n이 주어질 때 다음 조건을 만족하는
# 가장 큰 정수 i를 return
# n의 범위는 0 < n ≤ 3,628,800 이고 3,628,800은 10!

from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k