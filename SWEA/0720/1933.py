import sys

sys.stdin = open("1933.txt", "r")

n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end = ' ')

# n을 나누었을 때 나머지가 0인 것이 약수
# 약수를 구하기 위해 입력 받은 수까지 반복문을 돌림

# n + 1 을 하는 이유는
# 1부터 n보다 작을 때까지이기 때문에
# n은 반복하지 않아 + 1을 함