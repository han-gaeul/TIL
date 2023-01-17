# 별 찍기 2
# 첫째 줄에는 별 1개
# 둘째 줄에는 별 2개
# N번째 줄에는 별 N개
# 오른쪽을 기준으로 정렬한 별

N = int(input())

for i in range(1, N + 1):
    for j in range(N - i):
        print(' ', end = '')
    for j in range(i):
        print('*', end = '')
    print('')