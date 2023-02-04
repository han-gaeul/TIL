# 1920

# N개의 정수  A[1], A[2], ..., A[N]이 주어졌을 때
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하라

# 첫째 줄에 자연수 N이 주어진다
# 다음 줄에는 N개의 정수 A[1], A[2], ..., A[N]이 주어진다
# 다음 줄에는 M이 주어진다
# 다음 줄에는 M개의 수들이 주어지는데 이 수들이 A안에 존재하는지 알아낸다

# M개의 줄에 답을 출력
# 존재하면 1, 존재하지 않으면 0


# 이진 탐색
import sys

def binary_search(x, y):
    start = 0
    end = len(x) - 1
    while start <= end:
        mid = (start + end) // 2
        if y == x[mid]:
            return 1
        elif y > x[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

N = int(sys.stdin.readline())
a_list = list(map(int, sys.stdin.readline().split()))
a_list.sort()
M = int(sys.stdin.readline())
x_list = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    print(binary_search(a_list, x_list[i]))



# 이진탐색 : 정렬된 자료를 반으로 나누어 탐색하는 방법
# 주의할 점은 오름차순으로 정렬된 자료여야 한다



# set
# 시간은 이진탐색보다 빠름
import sys

N = int(sys.stdin.readline())
a_list = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
x_list = list(map(int, sys.stdin.readline().split()))
for i in x_list:
    print(1) if i in a_list else print(0)