# 다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한
# 위, 아래, 좌, 우, 대각선 칸을 모두 위험지역으로 분류한다
# 지뢰는 2차원 배열 board에 1로 표시되어 있고
# board에는 지뢰가 매설된 지역 1과, 지뢰가 없는 지역 0만 존재
# 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때
# 안전한 지역의 칸 수를 return

def solution(board):
    n = len(board)
    # 지뢰가 설치된 곳을 기준으로
    # 상하좌우, 대각선 칸을 모두 위험지역으로 분류
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    # 지뢰가 설치된 곳 찾기
    booms = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                booms.append((i, j))

    # 지뢰가 설치된 곳 주변을 위험지역으로 분류
    for i, j in booms:
        for k in range(8):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 1
    
    # 위험지역이 아닌 곳만 카운트
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                cnt += 1
    return cnt