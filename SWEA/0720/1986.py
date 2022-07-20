import sys

sys.stdin = open("1986.txt", "r")

T = int(input())
for test in range(1, T + 1):
    n = int(input())
    result = 0
    for i in range(1, n + 1):
        if i % 2:
            result += i
        else:
            result -= i
    print(f'#{test} {result}')

# 2로 나누었을 때 나머지가 0이면 짝수
# 2로 나누었을 때 나머지가 1이면 홀수