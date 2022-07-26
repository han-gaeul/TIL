# 터렛
# a와 b는 터렛에 근무하는 직원. 인구수는 차지하지 않음
# c는 a와 b에게 상대편 d의 위치를 계산하라는 명령을 내림
# a와 b는 각각 자신의 위치에서 현재 적까지의 거리를 계산
# a의 좌표 (x1, y1), b의 좌표 (x2, y2)가 주어지고
# a가 계산한 d와의 거리 r1과 b가 계산한 d와의 거리 r2가 주어졌을 때
# d가 있을 수 있는 좌표의 수를 출력

# 첫째 줄에 테이트 케이스의 개수 T가 주어진다
# 한 줄에 x1, y1, r1, x2, y2, r2가 주어진다
# 만약 d가 있을 수 있는 위치의 개수가 무한대일 경우 -1 출력

import math
        
# T = int(input())
# for test_case in range(1, T + 1):

n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두 원의 거리(원의 방정식 활용)
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    # 두 원이 동심원이고 반지름이 같을 때
    if distance == 0 and r1 == r2 :
        print(-1)
    # 내접, 외접일 때
    elif abs(r1 - r2) == distance or r1 + r2 == distance:
        print(1)
    # 두 원이 서로 다른 두 점에서 만날 때
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)
    else:
        print(0)