# 1978

# 주어진 수 N개 중이서 소수가 몇 개인지 찾아서 출력

# 첫 줄에 수의 개수 N이 주어진다.
# 다음으로 N개의 수가 주어진다

# 주어진 수들 중 소수의 개수를 출력

N = int(input())
nums = list(map(int, input().split()))
cnt = 0

for i in nums:
    for j in range(2, i + 1):
        if i % j == 0:
            if i == j:
                cnt += 1
            break
print(cnt)