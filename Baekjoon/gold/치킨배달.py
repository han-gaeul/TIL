# 15686

# 크기가 N x N인 도시가 있다. 도시는 1 x 1크기의 칸으로 나누어져 있다
# 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다
# 도시의 칸은 (r, c)와 같은 형태로 나타내고 r행 c열 또는 위에서부터
# r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다
# 이 도시에 사는 사람들은 치킨을 매우 좋아한다
# 따라서 사람들은 '치킨 거리'라는 말을 주로 사용한다
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다
# 즉 치킨 거리는 집을 기준으로 정해지며 각각의 집은 치킨 거리를 가지고 있다
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다
# 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1 - c2|로 구한다
# 예를 들어 아래와 같은 지도를 갖는 도시를 살펴보자
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 1
# 0 0 0 1 2
# 0은 빈칸, 1은 집, 2는 치킨집이다
# (2, 1)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |2 - 1| + |1 - 2| = 2.
# (5, 5)에 있는 치킨집과의 거리는 |2 - 5| + |1 - 5| = 7이다
# 따라서 (2, 1)에 있는 집의 치킨 거리는 2이다
# (5, 4)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |5 - 1| + |4 -2| = 6,
# (5, 5)에 있는 치킨집과의 거리는 |5 - 5| + |4 - 5| = 1이다
# 따라서 (5, 4)에 있는 집의 치킨 거리는 1이다
# 이 도시에 있는 치킨집은 모두 같은 프랜차이즈이다.
# 프랜차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을
# 폐업시키려고 한다. 오랜 연구 끝에 이 도시에서 가장 수익을 
# 많이 낼 수 있는 치킨집의 개수를 최대 M개라는 사실을 알아내었다
# 도시에 있는 치킨집 중에서 최대 M개를 고르고 나머지 치킨집은
# 모두 폐업시켜야 한다. 어떻게 고르면 도시의 치킨 거리가 가장 작게 될지 구하라

# 첫째 줄에 N과 M이 주어진다
# 둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다
# 도시의 정보는 0, 1, 2로 이루어져 있고 0은 빈칸, 1은 집,
# 2는 치킨집을 의미한다. 집의 개수는 2N개를 넘지 않으며
# 적어도 1개는 존재한다
# 치킨집의 개수는 M보다 크거나 같고 13보다 작거나 같다

# 첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때
# 도시의 치킨 거리의 최솟값을 출력

from itertools import combinations

N, M = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(N))
res = 100000
# 집과 치킨집의 위치를 저장할 빈 리스트 생성
house = []
chicken = []
# city 리스트를 순회하며 집과 치킨집의 위치를 각각 리스트에 저장
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])
# 치킨집 리스트에서 M개의 원소를 조합한 리스트를 반환하고 조합을 탐색
for chic in combinations(chicken, M):
    # 현재 조합으로 구한 치킨 거리의 합을 저장할 변수 초기화
    cnt = 0
    # 집들을 순회하며 현재 조합으로 구한 치킨 거리 계산
    for i in house:
        # i번째 집과 가장 가까운 치킨집까지의 거리를 저장할 변수 초기화
        chic_cnt = 1000
        # 현재 조합에서 선택한 치킨집들을 순회하며
        # 가장 가까운 치킨집까지의 거리를 구함
        for j in range(M):
            chic_cnt = min(chic_cnt, abs(i[0] - chic[j][0]) + abs(i[1] - chic[j][1]))
        # i번째 집과 가장 가까운 치킨집까지의 거리를 cnt에 더함
        cnt += chic_cnt
    # 현재 조합으로 구한 치킨 거리의 합이 이전에 구한 값보다 작으면 res 갱신
    res = min(res, cnt)
print(res)