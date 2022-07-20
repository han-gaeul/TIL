import sys

sys.stdin = open("2019.txt", "r")

n = int(input())

for i in range(n + 1):
        print((2 ** i), end = ' ')

# 1번부터 8번을 더 곱해서 총 9회가 됨
# 따라서 for문의 range는 range(n + 1)을 사용

# 2 ** i 를 사용하면 i만큼 제곱수를 계산
# 2 ** 0. 2 ** 1, 2 ** 2, ... , 2 ** 8까지 계산