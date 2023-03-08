# 2636

# 정사각형 칸들로 이루어진 사각형 모양의 판이 있고 그 위에 얇은
# 치즈가 놓여있다. 판의 가장자리에는 치즈가 놓여 있지 않으며
# 치즈에는 하나 이상의 구멍이 있을 수 있다
# 이 치즈를 공기 중에 놓으면 녹게 되는데 공기와 접촉된 칸은
# 한 시간이 지나면 녹아 없어진다. 치즈의 구멍 속에는 공기가 없지만
# 구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 구멍 속으로 공기가
# 들어가게 된다. 치즈의 구멍을 둘러싼 치즈는 녹지 않고 'c'로 표시된
# 부분만 한 시간 후에 녹아 없어진다
# 입력으로 사각형 모양의 판의 크기와 한 조각의 치즈가 판 위에
# 주어졌을 때 공기 중에서 치즈가 모두 녹아 없어지는 데
# 걸리는 시간과 모두 녹기 한 시간 전에 남아있는 치즈조각이
# 놓여 있는 칸의 개수를 구하라

# 첫째 출에는 사각형 모양 판의 세로와 가로의 길이가 양의 정수로 주어진다
# 판의 가로줄의 모양이 윗 줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다
# 치즈가 없는 칸은 0, 치즈가 있는 칸은 1로 주어지며
# 각 숫자 사이에는 빈칸이 하나씩 있다

# 첫째 줄에는 치즈가 모두 녹아서 없어지는 데 걸리는 시간을 출력하고
# 둘째 줄에는 모두 녹기 한 시간 전에 남아있는 치즈 조각이 놓여
# 있는 칸의 개수를 출력

from collections import deque

def bfs():
    # 시작 지점을 큐에 넣음
    q = deque([(0, 0)])
    # 녹일 치즈의 위치를 저장할 큐를 만듦
    melt = deque([])
    while q:
        x, y = q.popleft()
        # 상하좌우 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위를 벗어나지 않고, 아직 방문하지 않았다면
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # 해당 위치를 방문 처리
                visited[nx][ny] = 1
                # 치즈가 없는 곳이라면 큐에 추가
                if cheese[nx][ny] == 0:
                    q.append((nx, ny))
                # 치즈가 있는 곳이라면 녹일 치즈 목록에 추가
                elif cheese[nx][ny] == 1:
                    melt.append((nx, ny))
    # 녹일 치즈의 위치를 모두 확인하고
    # 해당 위치의 치즈를 모두 0으로 바꿈
    for x, y in melt:
        cheese[x][y] = 0
    # 녹인 치즈의 개수 반환
    return len(melt)
n, m= map(int, input().split())
cheese = []
cnt = 0
for i in range(n):
    cheese.append(list(map(int, input().split())))
    cnt += sum(cheese[i])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = 1
while True:
    # 방문한 위치를 저장할 리스트 초기화
    visited = [[0] * m for _ in range(n)]
    # 이번에 녹일 치즈의 개수를 구함
    melt_cnt = bfs()
    # 녹인 치즈의 개수를 전체 치즈의 개수에서 뺌
    cnt -= melt_cnt
    # 녹인 치즈가 모두 녹았다면,
    # 현재 시간과 녹인 치즈의 개수를 출력하고 반복문 종료
    if cnt == 0:
        print(time, melt_cnt, sep='\n')
        break
    # 치즈가 모두 녹지 않았다면 시간 증가
    time += 1