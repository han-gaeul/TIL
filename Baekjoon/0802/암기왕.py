# 백준 2776
# 첫째 줄에 테스트케이스의 개수 T가 들어온다
# 다음 줄에는 수첩1에 적어놓은 정수의 개수 N이 입력
# 그 다음 줄에는 수첩1에 적혀 있는 정수들이 N개
# 그 다음 줄에는 수첩2에 적어 놓은 정수의 개수 M
# 다음 줄에는 수첩2에 적어 놓은 정수들이 입력으로 M개

# 수첩2에 적혀있는 M개의 숫자 순서대로
# 수첩1에 있으면 1, 없으면 0 출력

import sys
sys.stdin = open('암기왕.txt', 'r')

T = int(input())
# T = int(sys.stdin.readline())

for _ in range(T):
    N = int(input())
    # N = int(sys.stdin.readline())
    note1 = set(map(int, input().split()))
    # note1 = list(map(int, sys.stdin.readline().split()))

    M = int(input())
    # M = int(sys.stdin.readline())
    note2 = list(map(int, input().split()))
    # note2 = list(map(int, sys.stdin.readline().split()))

    for i in note2:
        if i in note1:
            print(1)
        else:
            print(0)