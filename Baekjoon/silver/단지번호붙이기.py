# 2667

# 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고 단지에 번호를 붙이려한다
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다
# 대각선상에 집이 있는 경우는 연결된 것이 아니다.
# 지도를 입력하여 단지수를 출력하고 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력

# 첫번째 줄에는 지도의 크기 N이 입력되고 그다음 N줄에는 각각 N개의 자료가 입력된다

# 첫번째 줄에는 총 단지수를 출력
# 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력


#1. DFS
N = int(input())
# N x N 크기의 지도를 2차원 리스트로 생성하여 입력 받음
graph = [list(map(int, input())) for _ in range(N)]
# 각 집을 방문한 여부를 저장하는 2차원 리스트 생성
visited = [[False] * N for _ in range(N)]
# 단지 내 집의 개수를 저장할 리스트 생성
cnt = []
def dfs(x, y):
    # 함수 내에서 전역 변수 house_cnt 사용
    global house_cnt
    # 방문한 집 표시
    visited[x][y] = True
    # 현재 위치가 집이면 house_cnt를 1 증가시킴
    if graph[x][y] == 1:
        house_cnt += 1
    # x, y 좌표 이동값 리스트 선언
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        # 이동한 위치
        nx, ny = x + dx[i], y + dy[i]
        # 이동한 위치가 지도를 벗어나지 않았을 경우
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            # 방문하지 않은 집이면 dfs 수행
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)
# 모든 집을 방문하면서 dfs 수행
for i in range(N):
    for j in range(N):
        # 집이 있고 방문하지 않았다면
        if graph[i][j] == 1 and not visited[i][j]:
            # house_cnt 초기화
            house_cnt = 0
            # dfs 수행
            dfs(i, j)
            # 단지 내 집의 개수를 cnt 리스트에 추가
            cnt.append(house_cnt)
cnt.sort()
print(len(cnt), *cnt, sep='\n')
# 44ms



# 2. BFS
from collections import deque

N = int(input())
# N x N 크기의 지도를 2차원 리스트로 생성하여 입력 받음
graph = [list(map(int, input())) for _ in range(N)]
# 각 집을 방문한 여부를 저장하는 2차원 리스트 생성
visited = [[False] * N for _ in range(N)]
# 단지 내 집의 개수를 저장할 리스트 생성
cnt = []
def bfs(x, y):
    global house_cnt
    visited[x][y] = True
    # 현재 위치가 집이면 house_cnt를 1 증가시킴
    if graph[x][y] == 1:
        house_cnt += 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 이동한 위치가 지도를 벗어나지 않았을 경우
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                # 아직 방문하지 않았고 다음 위치에 집이 있다면
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    # house_cnt를 증가시키고 다음 위치를 deque에 추가
                    house_cnt += 1
                    q.append((nx, ny))
# 모든 집을 방문하면서 bfs 수행
for i in range(N):
    for j in range(N):
        # 집이 있고 방문하지 않았다면
        if graph[i][j] == 1 and not visited[i][j]:
            house_cnt = 0
            bfs(i, j)
            cnt.append(house_cnt)
cnt.sort()
print(len(cnt), *cnt, sep='\n')
# 64ms



# 각 집은 그래프의 정점으로 생각할 수 있으며
# 집과 집이 연결되어 있으면 그래프의 간선으로 생각할 수 있다
# 이때 연결된 집들의 집합을 단지라고 정의하고
# 각 단지에 번호를 붙여 출력하는 문제