# 9469

# 250마일 길이의 철로 양 끝에 두 기차 A와 B가 있다
# A는 시속 10마일, B는 시속 15마일로 서로를 향해 출발했다
# 두 기차의 출발과 동시에 기차 A 앞에 붙어있던 파리 한 마리가
# 기차가 충돌할 때까지 시속 20마일로 두 기차 사이를 왔다갔다 한다
# 이때 파리가 이동한 거리는 몇 마일일까?
# 폰 노이만은 문제를 듣자마자 머리 속으로 무한 급수를 이용해 계산한 다음
# 1초도 지나지 않은 시간에 200마일이라고 대답했다
# 철로의 길이 D, 두 기차 A, B의 속도와 파리의 속도 F가 주어졌을 때
# 위 문제의 답을 구하라

# 첫째 줄에 테스트 케이스의 개수 P가 주어진다
# 각 테스트 케이스는 다섯 숫자 N, D, A, B, F로 이루어져 있다
# N은 테스트 케이스의 번호이고 D는 철로의 길이,
# A와 B는 두 기차의 속도, F는 파리의 속도이다

# 각 테스트 케이스마다 테스트 케이스 번호를 출력하고
# 두 기차가 충돌할 때까지 파리가 움직인 거리를 출력

P = int(input())
for _ in range(P):
    N, D, A, B, F = map(float, input().split())
    T = D / (A + B) * F
    print('%d %.6f' % (N, T))