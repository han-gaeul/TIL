# 구구단
# N을 입력 받은 뒤 구구단 N단을 출력
# 첫째 줄에 N이 주어진다.
# N은 1보다 크거나 같고 9보다 작거나 같다

N = int(input())

for i in range(1, 10):
    print(f'{N} * {i} = {N * i}')