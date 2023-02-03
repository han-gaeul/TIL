# 1021

# 지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다
# 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다
# 지민이는 이 큐에서 다음과 같은 3가지 원소를 수행할 수 있다
# 1. 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면 원래 큐의 원소가 a1, ... ak였던 것이 a2, ..., ak와 같이 된다
# 2. 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면 a1, ..., ak가 a2, ..., ak, a1이 된다.
# 3. 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면 a1, ..., ak가 ak, a1, ..., ak-1이 된다
# 큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다
# (이 위치는 가장 처음 큐에서의 위치이다.)
# 이때 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하라

# 첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다
# 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다

# 첫째 줄에 문제의 정답을 출력

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
dq = deque([i for i in range(1, N + 1)])
idx = list(map(int, sys.stdin.readline().split()))
cnt = 0
for num in idx:
    while 1:
        if dq[0] == num:
            dq.popleft()
            break
        else:
            if dq.index(num) <= len(dq) // 2:
                dq.rotate(-1)
                cnt += 1
            else:
                dq.rotate(1)
                cnt += 1
print(cnt)