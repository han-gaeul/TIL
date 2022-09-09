# 2차원 평면 위의 점 N개가 주어진다
# 좌표를 x 좌표가 증가하는 순으로
# x 좌표가 같으면 y 좌표가 증가하는 순서로 정렬한 다음 출력

# 첫째 줄에 점의 개수 N이 주어진다
# 둘째 줄부터 N개의 줄에는 I번점의 위치 x1과 y1이 주어진다

# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력

import sys
input = sys.stdin.readline

N = int(input())
nums = []

for _ in range(N):
    [x, y] = map(int, input().split())
    nums.append([x, y])

s_nums = sorted(nums)

for i in range(N):
    print(s_nums[i][0], s_nums[i][1])

