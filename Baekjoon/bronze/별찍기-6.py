# 2443

# 첫째 줄에는 별 2 x N - 1개, 둘째 줄에는 별 2 x N - 3개, ..., N번째 줄에는 별 1개를 찍는 문제
# 별은 가운데를 기준으로 대칭이어야 한다

# 첫째 줄에 N이 주어진다

# 첫째 줄부터 N번째 줄까지 차례대로 별 출력

N = int(input())
for i in range(N, 0, -1):
    print(' ' * (N - i) + '*' * (2 * i - 1))