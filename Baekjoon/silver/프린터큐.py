# 1966

# 프린터 기기는 인쇄하고자 하는 문서를 인쇄 명령을 받은 순서대로, 즉 먼저 요청된 것을 먼저 인쇄한다
# 여러 개의 문서가 쌓인다면 Queue 자료 구조에 쌓여서 FIFO에 따라 인쇄가 된다
# 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발했는데 이 프린터기는 다음과 같은 조건에 따라 인쇄한다
# 1. 현재 Queue의 가장 앞에 있는 문서의 '중요도'를 확인
# 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면
# 이 문서를 먼저 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄
# 예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3이라면 C를 인쇄하고
# 다음으로 D, A, B를 인쇄하게 된다
# 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때 어떤 한 문서가
# 몇 번째로 인쇄되는지 알아내자. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄된다

# 첫 줄에 테스트 케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다
# 테스트케이스의 첫 번째 줄에는 문서의 개수 N과, 몇 번째로 인쇄 되었는지 궁금한 문서가
# 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M이 주어진다
# 이때 맨 왼쪽은 0번째라고 하자.
# 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다
# 중요도는 1 이상 9 이하의 정수이고 중요도가 같은 문서가 여러개 있을 수 있다

# 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄 되는지 출력

import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    N, M = map(int, sys.stdin.readline().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    idx = deque(list(range(N)))
    # 몇 번째로 인쇄된 것인지 셀 변수 선언
    cnt = 0
    while queue:
        # 가장 앞에 있는 문서의 중요도 확인
        if queue[0] == max(queue):
            cnt += 1
            queue.popleft()
            if idx.popleft() == M:
                print(cnt)
        else:
            queue.append(queue.popleft())
            idx.append(idx.popleft())