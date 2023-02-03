# 10866

# 정수를 저장하는 덱(Deque)을 구현한 다음 입력으로 주어지는 명령을 처리하라
# 명령은 총 여덟가지이다
# push_front X : 정수 X를 덱의 앞에 넣는다
# push_back X : 정수 X를 덱의 뒤에 넣는다
# pop_front : 덱에 가장 앞에 있는 수를 빼고 그 수를 출력
# 만약 덱에 들어있는 정수가 없다면 -1 출력
# pop_back : 덱에 가장 뒤에 있는 수를 빼고 그 수를 출력
# 만약 덱에 들어있는 정수가 없다면 -1 출력
# size : 덱에 들어있는 정수의 개수 출력
# empty : 덱이 비어있으면 1, 아니면 0 출력
# front : 덱의 가장 앞에 있는 정수 출력
# 만약 덱에 들어있는 정수가 없다면 -1 출력
# back : 덱의 가장 뒤에 있는 정수 출력
# 만약 덱에 들어있는 정수가 없다면 -1 출력

# 첫째 줄에 주어지는 명령의 수 N이 주어진다
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다
# 문제에 나와있지 않은 명령이 주어지는 경우는 없다

# 출력해야 하는 명령이 주어질 때마다 한 줄에 하나씩 출력

import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque()
for _ in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push_front':
        dq.appendleft(command[1])
    elif command[0] == 'push_back':
        dq.append(command[1])
    elif command[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif command[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif command[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])