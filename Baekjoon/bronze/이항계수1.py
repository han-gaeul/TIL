# 11050

# 자연수 N과 정수 K가 주어졌을 때 이항 계수를 구하라

# 첫째 줄에 N과 K가 주어진다

import math

n, k = map(int, input().split())
print(math.comb(n, k))