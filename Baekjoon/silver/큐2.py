# 18258

# 정수를 저장하는 큐를 구현한 다음 입력으로 주어지는 명령을 처리하라
# 명령은 총 여섯 가지이다
# push X : 정수 X를 큐에 넣는 연산
# pop : 큐에서 가장 앞에 있는 정수를 빼고 그 수를 출력
# 만약 큐에 들어있는 정수가 없는 경우 -1 출력
# size : 큐에 들어있는 정수의 개수를 출력
# empty : 큐가 비어있으면 1, 아니면 0 출력
# front : 큐의 가장 앞에 있는 정수 출력
# 만약 큐에 들어있는 정수가 없다면 -1 출력
# back : 큐의 가장 뒤에 있는 정수 출력
# 만약 큐에 들어있는 정수가 없다면 -1 출력

# 첫째 줄에 주어지는 명령의 수 N이 주어진다
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다
# 문제에 나와있지 않은 명령이 주어지는 경우는 없다

# 출력 해야 하는 명령이 주어질 때마다 한 줄에 하나씩 출력

import sys
from collections import deque
queue = deque()
for i in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if not queue:
            print(-1)
        else:
            # 첫번째 값 출력 후
            print(queue[0])
            # 첫번째 값 제거
            queue.popleft()
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])



# deque는 앞, 뒤에서 데이터를 처리할 수 있는 양방향 자료형
# 스택, 큐 둘 다 사용 가능