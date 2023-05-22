# 문자열 my_string과 두 정수 m, c가 주어진다
# my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로
# c번째 열에 적힌 글자들을 문자열로 return

def solution(my_string, m, c):
    rows = len(my_string) // m
    col = m
    grid = [[my_string[i * m + j] for j in range(col)] for i in range(rows)]
    ans = ''.join(grid[i][c - 1]for i in range(rows))
    return ans