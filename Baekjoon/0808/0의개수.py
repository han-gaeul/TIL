# 11170
# N부터 M까지의 수들을 종이에 적었을 때
# 종이에 적힌 0들을 세는 프로그램 작성
# 예 : N. M이 각각 0, 10일때 0을 세면
# 0에 하나 10에 하나가 있으므로 답은 2

# 첫번째 줄에 테스트 케이스의 수 T가 주어진다
# 각 줄에는 N과 M이 주어진다

# 출력예시
# 2
# 199
# 0

import sys
sys.stdin = open('0의개수.txt')

T = int(input())

for _ in range(1, T + 1):
    N, M = map(int, input().split())
    count = 0

    #* N부터 M까지의 수
    for i in range(N, M + 1):
        w = str(i)
        #* w에 '0'이 있으면 count
        count += w.count('0')
    print(count)