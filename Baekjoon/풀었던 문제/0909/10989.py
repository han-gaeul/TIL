# N개의 수가 주어졌을 때 이를 오름차순으로 정렬하는 프로그램 작성

# 첫째 줄에 수의 개수 N이 주어진다
# 둘째 줄부터 N개의 줄에는 수가 주어진다

# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를
# 한 줄에 하나씩 출력

# 메모리 초과
# import sys

# N = int(input())
# nums = []

# for i in range(N):
#     nums.append(sys.stdin.readline())

# for i in sorted(nums):
#     sys.stdout.write(str(i)+'\n')


#! ---------------------------------------

# 정답

import sys

N = int(sys.stdin.readline())
nums = [0] * 10001

for i in range(N):
    nums[int(sys.stdin.readline())] += 1

for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)

# for문 안에서 append를 사용하게 되면 메모리 재할당이 이루어져
# 메모리를 효율적으로 사용하지 못한다
# 입력값이 크지 않은 경우에는 상관 없지만 입력값이 커질 때는 메모리 초과 됨
# 입력값이 10000개까지 부어질 수 있으니 10000개 만큼의 리스트를 만듦
# 인덱스는 0부터 세기 때문에 길이가 10001인 리스트
# 리스트에 각 요소마다 0을 할당하고 입력값을 받을 떄마다
# 그 입력값과 같은 인덱스에 1씩 더한다
# 입력을 다 받고 나면 0보다 큰 요소를 갖는 인덱스를 찾아서
# 그 수만큼 인덱스를 출력한다