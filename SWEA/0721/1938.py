import sys

sys.stdin = open("1938.txt", "r")

# 두 개의 자연수를 입력 받아 사칙연산을 수행하는 프로그램
# a, b는 1부터 9까지의 자연수
# +, -, *, / 순서로 연산한 결과를 출력
# 나누기 연산 결과에서 소수점 이하의 숫자는 버린다 -> 몫만 출력

a,b = map(int, input().split())

# for i in range(1, 10):
print(a + b)
print(a - b)
print(a * b)
print(a // b)