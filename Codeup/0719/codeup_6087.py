n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i, end = ' ') # 홀수가 아닐 때만 실행
