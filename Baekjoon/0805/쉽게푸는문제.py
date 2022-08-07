# 1292
# 1을 한 번, 2를 두 번, 3을 세 번 이런 식으로 1 2 2 3 3 3 4 4 4 4 ...
# 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것

# 첫째 줄에 구간의 시작과 끝을 나타내는 정수 A, B 가 주어진다
# 수열에서 A번째 숫자부터 B번째 숫자까지 합을 구하면 된다

import sys
sys.stdin = open('쉽게푸는문제.txt')

A, B = map(int, input().split())
arr = []

for i in range(B + 1):
    for j in range(i):
        if len(arr) == B:
            break
        arr.append(i)
print(sum(arr[A - 1 : B]))