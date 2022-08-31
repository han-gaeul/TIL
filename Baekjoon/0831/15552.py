# 첫 줄에 테스트 케이스의 개수 T가 주어진다
# 다음 T줄에는 각각 두 정수 A와 B가 주어진다

# 각 테스트케이스마다 A + B를 한 줄에 하나씩 출력

import sys

# input으로 실행하면 시간 초과 에러 발생
T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)