# 9 * 9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때
# 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하라

# 첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다


board = [list(map(int, input().split())) for _ in range(9)]

print(max(board))
print(board.index(max(board)) + 1)

# 백준에서 계속 틀렸다고 함
# why?!??!????
# 내일 다시 풀기