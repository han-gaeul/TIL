import sys

sys.stdin = open("1976.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())

    m = m1 + m2
    # m이 60이 넘어가면 60으로 나눠서 몫을 h에 더함
    h = h1 + h2 + m // 60
    # 마찬가지로 m이 60이 넘어가면 60으로 나눈 나머지를 m에 할당
    m = m % 60
    # h가 12보다 크면 h에서 12를 뺌
    if h > 12:
        h -= 12
    print('#{} {} {}'.format(test_case, h, m))