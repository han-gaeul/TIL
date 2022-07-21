import sys

sys.stdin = open("2043.txt", "r")

# 서랍 비밀번호 구하기
# 비밀번호 P는 000부터 999까지 번호 중 하나
# 주어지는 번호 K부터 1씩 증가하며 비밀번호를 확인

# 예를 들어 비밀번호 P가 123이고 주어지는 번호 K가 100일 때
# 100부터 123까지 24번 확인하여 비밀번호를 맞출 수 있다.
# P와 K가 주어지면 K부터 시작하여 몇 번만에 P를 맞출 수 있는지?

P, K = map(int, input().split())

count = 0

for i in range(K, P + 1):
    if K != P:
        count += 1
    else:
        count = 1
print(count)