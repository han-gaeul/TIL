# 1929

# M 이상 N 이하의 소수를 모두 출력

# 첫째 줄에 자연수 M, N이 빈 칸을 사이에 두고 주어진다

# 한 줄에 하나씩 증가하는 순서대로 소수를 출력

m, n = map(int, input().split())

for i in range(m, n + 1):
    # 1은 소수가 아님
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i)