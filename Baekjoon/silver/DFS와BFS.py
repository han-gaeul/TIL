# 1260

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력
# 단 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문하고
# 더이상 방문할 수 있는 점이 없는 경우 종료한다
# 정점 번호는 1번부터 N번까지이다

# 첫째 줄에 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V가 주어진다
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다
# 입력으로 주어지는 간선은 양방향이다

# 첫째 줄에 DFS를 수행한 결과를,
# 그 다음 줄에는 BFS를 수행한 결과를 출력
# V부터 방문된 점을 순서대로 출력

from collections import deque

# start : 시작 노드
def dfs(start):
    # 방문한 노드를 저장한 리스트 초기화
    visited = [False] * (N + 1)
    # 스택을 초기화하고 시작 노드 추가
    stack = [start]
    # 방문한 노드를 저장할 리스트 초기화
    res = []
    # 스택이 비어있을 때까지 반복
    while stack:
        # 스택에서 노드를 꺼냄
        node = stack.pop()
        # 아직 방문하지 않은 노드인 경우
        if not visited[node]:
            # 노드를 방문 처리하고 결과 리스트에 추가
            visited[node] = True
            res.append(node)
            # 노드의 인접한 노드를 스택에 추가
            for next in sorted(graph[node], reverse=True):
                if not visited[next]:
                    stack.append(next)
    return res
def bfs(start):
    visited = [False] * (N + 1)
    # 큐를 초기화하고 시작 노드 추가
    queue = deque([start])
    # 시작 노드를 방문 처리하고 결과 리스트에 추가
    visited[start] = True
    res = [start]
    while queue:
        # 큐에서 노드를 꺼냄
        node = queue.popleft()
        # 노드의 인접한 노드 방문
        for next in sorted(graph[node]):
            # 인접한 노드가 아직 방문하지 않은 노드인 경우
            if not visited[next]:
                # 노드를 방문 처리하고 결과 리스트에 추가
                visited[next] = True
                res.append(next)
                # 노드를 큐에 추가
                queue.append(next)
    return res
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    # 간선의 정보를 입력 받아 인접 리스트에 추가
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(*dfs(V))
print(*bfs(V))