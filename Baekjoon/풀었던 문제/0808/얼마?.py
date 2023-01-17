# 9325
# 첫째 줄에 테스트 케이스의 개수가 주어진다
# 각 테스트 케이스의 첫 줄엔 자동차의 가격 s가 주어진다
# 둘째 줄엔 구매하려고 하는 서로 다른 옵션의 개수 n이 주어진다
# 뒤이어 n개의 줄이 입력으로 들어온다
# 각 줄은 q와 p로 이루어져 있는데 q는 사려고 하는 특정 옵션의 개수
# p는 해당 옵션의 가격

# 최종적으로 구매하려는 자동차의 가격을 한 줄씩 출력

# 출력 예시
# 13200
# 50000

import sys
sys.stdin = open('얼마?.txt')

T = int(input())

for _ in range(T):
    s = int(input())
    n = int(input())

    for _ in range(n):
        q, p = map(int, input().split())
        s += q * p
    
    print(s)