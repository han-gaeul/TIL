# 10991

# 예제를 보고 규칙을 유추한 뒤에 별을 찍어라

# 첫째 줄에 N이 주어진다

# 첫째 줄부터 N번째 줄까지 차례대로 별 출력

N = int(input())
for i in range(1, N + 1):
    print(' ' * (N - i) + '* ' * (i - 1) + '*')