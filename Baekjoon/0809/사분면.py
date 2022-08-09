# 9610
# 2차원 좌표 상의 여러 점의 좌표 (x, y)가 주어졌을 때
# 각 사분면과 축에 점이 몇 개 있는지 구하는 프로그램

# 첫째 줄에 점의 개수 n이 주어진다
# 다음 n개 줄에는 점의 좌표 (xi, yi)가 주어진다

# 출력 예시
# Q1: 2
# Q2: 0
# Q3: 0
# Q4: 1
# AXIS: 2

import sys
sys.stdin = open('사분면.txt')

n = int(input())

for _ in range(n):
    xi, yi = map(int, input().split())
    print(xi, yi)