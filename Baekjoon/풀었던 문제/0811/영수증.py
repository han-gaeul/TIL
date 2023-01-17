# 25304
# 영수증을 보면서 정확하게 계산된 것이 맞는지 확인
# 1. 구매한 각 물건의 가격과 개수
# 2. 구매한 물건들의 총 금액
# 두 조건을 보고 구매한 물건의 가격과 개수로 계산한
# 총 금액이  영수증에 적힌 총 금액과 일치하는지 검사

# 첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다
# 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다
# 이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 주어진다

# 구매한 물건의 가격과 개수로 계산한 총 금액이
# 영수증에 적힌 총 금액과 일치하면 Yes
# 일치하지 않는다면 No

import sys
sys.stdin = open('영수증.txt')

X = int(input())
N = int(input())

sum_ = []

for _ in range(N):
    a, b = map(int, input().split())
    sum_.append(a * b)
    
if sum(sum_) == X:
    print('Yes')
else:
    print('No')