import sys

sys.stdin = open("2025.txt", "r")

# 1부터 주어진 숫자만큼 모두 더한 값을 출력
# 단, 주어질 숫자는 10000을 넘지 않는다.

n = int(input())

sum = 0

for i in range(1, n + 1):
    sum += i
print(sum)

# 입력 받은 숫자를 하나씩 i에 담아서
# sum 함수를 이용해 하나씩 더함