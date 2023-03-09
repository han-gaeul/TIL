# 2583

# 눈금의 간격이 1인 M x N 크기의 모눈종이가 있다
# 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때
# 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된
# 영역으로 나누어진다.
# M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때
# K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 
# 영역으로 나누어지는지, 그리고 분리된 각 영역의 넓이가
# 얼마인지를 구하라

# 첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다
# 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래
# 꼭짓점의 x, y 좌표값과 오른쪽 위 꼭짓점의 x, y 좌표값이 
# 빈칸을 사이에 두고 차례로 주어진다
# 모눈 종이의 왼쪽 아래 꼭짓점의 좌표는 (0, 0)이고
# 오른쪽 위 꼭짓점의 좌표는 (N, M)이다
# 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다

# 첫째 줄에 분리되어 나누어지는 영역의 개수를 출력
# 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여
# 빈칸을 사이에 두고 출력

import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())
graph = [[0] * N for _ in range(M)]
# 직사각형 그리기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
# 방문 체크 리스트 초기화
visited = [[False] * N for _ in range(M)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# 분리된 영역의 크기를 담을 리스트
areas = []
def bfs(x, y):
    # 시작점도 영역 크기에 포함되므로 1로 초기화
    cnt = 1
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위를 벗어나거나 방문한 적이 있거나
            # 그래프의 값이 1인 경우 건너뜀
            if nx < 0 or ny < 0 or nx >=M or ny >= N:
                continue
            if not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    return cnt
for i in range(M):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 0:
            areas.append(bfs(i, j))
areas.sort()
print(len(areas), *areas, sep='\n')