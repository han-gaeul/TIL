from math import remainder
import sys

sys.stdin = open("2029.txt", "r")



T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    quotient, remainder = a // b, a % b
    # 줄바꿈 없이 변수 지정 가능

    print('#{} {} {}'.format(test_case, quotient, remainder))
