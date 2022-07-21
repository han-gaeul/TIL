import sys

sys.stdin = open("1936.txt", "r")

# A와 B가 가위바위보를 함
# 가위는 1, 바위는 2, 보는 3
# A와 B 중에 누가 이겼는지? 단, 비기는 경우는 없음
# A가 이기면 A, B가 이기면 B를 출력

A, B = map(int, input().split())

if A > B:
    print('A')
else:
    print('B')