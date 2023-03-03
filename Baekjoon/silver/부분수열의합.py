# 1182

# N개의 정수로 이루어진 수열이 있을 때
# 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이
# S가 되는 경우의 수를 구하라

# 첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다
# 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다

# 첫째 줄에 합이 S가 되는 부분수열의 개수를 출력

import itertools

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, N + 1):
    # 리스트에서 i개의 원소로 이루어진 모든 부분집합을 구하고 nums 변수에 저장
    for nums in itertools.combinations(arr, i):
        if sum(nums) == S:
            cnt += 1
print(cnt)