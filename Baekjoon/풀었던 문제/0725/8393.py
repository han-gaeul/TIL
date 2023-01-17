# 합
# n이 주어졌을 때 1부터 n까지 합 출력

n = int(input())

result = int()

for i in range(1, n + 1):
    result += i
print(result)