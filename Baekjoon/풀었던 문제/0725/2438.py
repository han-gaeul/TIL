# 별 찍기
# 첫째 줄에는 별 1개
# 둘째 줄에는 별 2개
# N번째 줄에는 별 N개

N = int(input())

for i in range(0, N):
    for j in range(i + 1):
        print('*', end = '')
    print('')