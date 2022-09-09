# 2차원 평면 위의 점 N개가 주어진다
# 좌표를 y 좌표가 증가하는 순으로 y 좌표가 같으면
# x 좌표가 증가는 순서로 정렬한 다음 출력

# 첫째 줄에 점의 개수 N이 주어진다
# 둘째 줄부터 N개의 줄에는 i번점의 위치 x와 y가 주어진다

# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력

import sys
input = sys.stdin.readline

N = int(input())
nums = []

for _ in range(N):
    x, y = map(int, input().split())
    # 출력 값이 y를 기준으로 정렬되게 리스트에 y, x 순서로 append
    nums.append([y, x])

s_nums = sorted(nums)

for i in range(N):
    print(s_nums[i][1], s_nums[i][0])