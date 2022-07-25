# 최소, 최대
# N개의 정수가 주어진다
# 이때 최솟값과 최댓값을 출력

# 첫째 줄에 정수의 개수 N이 주어진다
# 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다
# 첫째 줄에 주어진 정수 N개의 최소값과 최댓값을 공백으로 구분해 출력

N = int(input())
N_list = list(map(int, input().split()))

print(min(N_list), max(N_list))