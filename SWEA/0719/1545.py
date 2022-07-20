import sys

sys.stdin = open("1545.txt", "r")

n = int(input())

for i in range(n, -1, -1):
    print(n, end = ' ')
    n = n - 1