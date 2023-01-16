# N * M 크기의 두 행렬 A와 B가 주어졌을 때
# 두 행렬을 더하라

# 첫째 줄에 행렬의 크기 N과 M이 주어진다
# 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가
# 차례대로 주어진다. 이어서 N개의 줄에
# 행렬 B의 원소 M개가 차례대로 주어진다.


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        A[i][j] += B[i][j]
        print(A[i][j], end=' ')