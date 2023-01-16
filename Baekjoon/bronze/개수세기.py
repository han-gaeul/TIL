# 총 N개의 정수가 주어졌을 때 정수 v가 몇 개인지 구하라
# 첫째 줄에 정수의 개수 N이 주어진다
# 둘째 줄에는 정수가 공백으로 구분 되어있다
# 셋째 줄에는 찾으려고 하는 정수 v가 주어진다


N = int(input())
num_list = list(map(int, input().split()))
find_num = int(input())


# 1.
result = 0

for i in num_list:
    if find_num == i:
        result += 1

print(result)


# 2.
result = sum(1 for i in num_list if find_num == i)

print(result)