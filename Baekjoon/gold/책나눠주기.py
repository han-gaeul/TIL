# 9576

# 백준이는 방 청소를 하면서 필요 없는 전공 서적을 사람들에게
# 나눠주려고 한다. 나눠줄 책을 모아보니 총 N권이었다
# 책이 너무 많기 때문에 백준이는 책을 구분하기 위해 각각
# 1부터 N까지의 정수 번호를 중복되지 않게 매겨 두었다
# 조사를 해 보니 책을 원하는 서강대학교 학부생이 총 M명이었다
# 백준이는 이 M명에게 신청서에 두 정수 a, b를 적어 내라고 했다
# 그러면 백준이는 책 번호가 a 이상 b 이하인 책 중 남아있는
# 책 한 권을 골라 그 학생에게 준다. 만약 a번부터 b번까지의
# 모든 책을 이미 다른 학생에게 주고 없다면 그 학생에게는
# 책을 주지 않는다
# 백준이가 책을 줄 수 있는 최대 학생 수를 구하라

# 첫째 줄에 테스트 케이스의 수가 주어진다
# 각 케이스의 첫 줄에 정수 N과 M이 주어진다
# 다음 줄부터 M개의 줄에는 각각 정수 ai, bi가 주어진다

# 각 테스트 케이스마다 백준이가 책을 줄 수 있는 최대
# 학생 수를 한 줄에 하나씩 출력

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    books = [False] * (N + 1)
    req = []
    for _ in range(M):
        req.append(list(map(int, sys.stdin.readline().split())))
    # 신청서의 마감일을 기준으로 정렬
    req.sort(key=lambda x : x[1])
    # 학생들에게 책을 나눠줄 횟수를 카운트할 변수 초기화
    cnt = 0
    for a, b in req:
        # 요청한 범위 내에서 가장 번호가 작은 책을 줌
        for i in range(a, b + 1):
            if not books[i]:
                cnt += 1
                books[i] = True
                break
    print(cnt)