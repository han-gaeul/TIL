# 머쓱이는 구슬을 친구들에게 나누어주려고 한다
# 구슬은 모두 다르게 생겼다. 머쓱이가 가지고 있는 구슬의 개수
# balls와 친구들에게 나누어 줄 구슬 개수 share이
# 매개변수로 주어질 때 balls개의 구슬 중 share개의
# 구슬을 고르는 가능한 모든 경우의 수를 return

import math

def solution(balls, share):
    return math.comb(balls, share)

# comb(n, k)
# nCk와 같은 조합 값을 반환
# 조합은 n개의 수 중 k개를 꺼내는 수와 동일
# n개의 수는 모두 같은 수라고 가정
# n과 k는 모두 int값만 가능