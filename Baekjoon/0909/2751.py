# N개의 수가 주어졌을 때 이를 오름차순으로 정렬하는 프로그램 작성

# 첫째 줄에 수의 개수 N이 주어진다
# 둘째 줄부터 N개의 줄에는 수가 주어진다
# 수는 중복되지 않는다

# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를
# 한 줄에 하나씩 출력한다.

import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))
    
for i in sorted(nums):
    sys.stdout.write(str(i)+'\n')