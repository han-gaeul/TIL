# 5988

# 짝이 없는 경재는 매일 홀로 있다보니 홀수를 판별할 수 있는 능력이 생겼다
# 창식이는 경재의 말이 사실인지 그 능력을 시험해보려 한다
# 창식이의 의심이 끝이 없을 것 같아 N개만 확인하기로 했다
# N개의 정수가 주어지면 홀수인지 짝수인지를 출력하라

# 첫번째 줄에 숫자의 개수 N이 주어진다
# 두번째 줄부터 N + 1번째 줄에 걸쳐 홀수인지 짝수인지 확인할 정수 K가 주어진다

# N개의 줄에 걸쳐 한 줄씩 정수 K가 홀수라면 'odd'
# 짝수라면 'even'을 출력

N = int(input())
for _ in range(N):
    K = int(input())
    print('even' if K % 2 == 0 else 'odd')