# 9663

# N-Queen 문제는 크기가 N x N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다
# N이 주어졌을 때 퀸을 놓는 방법의 수를 구하라

# 첫째 줄에 N이 주어진다

# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력


# 1.
arr = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(arr[int(input())])
# 40ms
# 문제의 범위가 15 x 15로 정해져있음


# 2.
n = int(input())
arr = [0] * n
cnt = 0
def check(x):
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[x] - arr[i]) == x - i:
            return 0
    return 1
def dfs(x):
    global cnt
    if x == n:
        cnt += 1
        return
    for i in range(n):
        arr[x] = i
        if check(x):
            dfs(x + 1)
dfs(0)
print(cnt)
# python3으로 제출하면 시간초과
# pypy3으로 제출하면 정답 처리 됨
# 29424ms


# 3.
n = int(input())
board = [0] * n
res = 0
visited = [False] * n
def check(x):
    for i in range(x):
        if abs(board[x] - board[i]) == x - i:
            return False
    return True
def dfs(x):
    global res
    if x == n:
        res += 1
        return
    for i in range(n):
        if visited[i]:
            continue
        board[x] = i
        if check(x):
            visited[i] = True
            dfs(x + 1)
            visited[i] = False
dfs(0)
print(res)
# pypy3으로 제출하면 정답 처리 됨
# python3으로 제출하면 시간초과
# 12544ms