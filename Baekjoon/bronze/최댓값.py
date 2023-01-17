# 9 * 9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때
# 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하라

# 첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다


board = [list(map(int, input().split())) for _ in range(9)]

print(max(board))
print(board.index(max(board)) + 1)

# 백준에서 계속 틀렸다고 함
# why?!??!????
# 내일 다시 풀기


board = [list(map(int, input().split())) for _ in range(9)]

max_num, max_row, max_col = 0

for row in range(9):
    for col in range(9):
        if max_num <= board[row][col]:
            max_row = row + 1
            max_col = col + 1
            max_num = board[row][col]

print(max_num)
print(max_row, max_col)


# for문을 최대한 반복하지 않으려고 위에 있는 코드로 작성했는데
# 위는 오답, 밑은 정답 처리가 됐다... 뭘까..
# max, index 같은 함수를 사용해서 그럴까..?