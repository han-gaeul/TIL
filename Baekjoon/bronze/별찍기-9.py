# 2446

# 예제를 보고 규칙을 유추한 뒤 별을 찍어라

# 첫째 줄에 N이 주어진다

# 첫째 줄부터 2 x N - 1번째 줄까지 차례대로 별을 출력

# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

N = int(input())
for i in range(1, N + 1):
    print(' ' * (i - 1) + '*' * (2 * (N - i) + 1))
for i in range(1, N):
    print(' ' * (N - i - 1) + '*' * ((2 * i) + 1))