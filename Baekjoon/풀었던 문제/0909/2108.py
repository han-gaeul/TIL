# 통계학에서 N개의 수를 대표하는 기본 통계값에는
# 다음과 같은 것들이 있다. 단, N은 홀수라고 가정
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열 했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때 네 가지 기본 통계값을 구하는 프로그램 작성

# 첫째 줄에 수의 개수 N이 주어진다. 단 N은 홀수
# 그 다음 N개의 줄에는 정수들이 주어진다

# 첫째 줄에는 산술평균을 출력. 소수점 이하 첫째 자리에서 반올림한 값 출력
# 둘째 줄에는 중앙값 출력
# 셋째 줄에는 최빈값 출력. 여러 개 있을 때는 최빈값 중 두 번째로 작은 값 출력
# 넷째 줄에는 범위 출력

import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

# 산술평균 : 다 더하고 / N
print(round(sum(nums) / N))

# 중앙값 : 오름차순 정렬 후 중간값
nums.sort()
print(nums[N // 2])

# 최반값 : 빈출
count_nums = Counter(nums).most_common()
if len(count_nums) >1 and count_nums[0][1] == count_nums[1][1]:
    print(count_nums[1][0])
else:
    print(count_nums[0][0])

# 범위 : 최댓값 - 최솟값
print(max(nums) - min(nums))
