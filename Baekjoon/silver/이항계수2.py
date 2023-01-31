# 11051

# 자연수 N과 정수 K가 주어졌을 때 이항 계수를 10,007로 나눈 나머지를 구하라

# 첫째 줄에 N과 K가 주어진다

# 10,007로 나눈 나머지를 출력

import math

n, k = map(int, input().split())
nk = math.comb(n, k)
print(nk % 10007)