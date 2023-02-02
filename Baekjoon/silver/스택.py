# 10828

# 정수를 저장하는 스택을 구현한 다음 입력으로 주어지는 명령을 처리
# 명령은 총 다섯가지이다
# push X : 정수 X를 스택에 넣는 연산
# pop : 스택에서 가장 위에 있는 정수를 빼고 그 수를 출력
# 만약 스택에 들어있는 정수가 없는 경우 -1 출력
# size : 스택에 들어있는 정수의 개수 출력
# empty : 스택이 비어있으면 1, 아니면 0 출력
# top : 스택의 가장 위에 있는 정수 출력
# 만약 스택에 들어있는 정수가 없는 경우 -1 출력

# 첫째 줄에 주어지는 명령의 수 N이 주어진다
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다
# 문제에 나와있지 않은 명령이 주어지는 경우는 없다

# 출력 해야 하는 명령이 주어질 때마다 한 줄에 하나씩 출력

import sys
stack = []
for i in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])