# 9개의 서로 다른 자연수가 주어질 때
# 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지 구하라

# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다

# 첫째 줄에 최댓값을 출력하고 둘째 줄에 최댓값이 몇 번째 수인지를 출력

num_list = []

for i in range(1, 10):
    num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list)) + 1)