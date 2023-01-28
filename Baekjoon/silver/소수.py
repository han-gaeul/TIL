# 2581

# 자연수 M과 N이 주어질 때 M 이상 N 이하의 자연수 중
# 소수인 것을 모두 골라 이들 소수의 합과 최소삾을 찾는 프로그램을 작성
# 예를 들어, M = 60, N = 100인 경우 60 이상 100 이하의 자연수 중
# 소수는 61, 67, 71, 79, 83, 89, 97 총 8개가 있으므로
# 이들 소수의 합은 620이고 최솟값은 61이 된다

# 입력의 첫째 줄에 M이 둘째 줄에 N이 주어진다

# M 이상 N 이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을,
# 둘째 줄에 그 중 최솟값을 출력한다
# 단, M 이상 N 이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1 출력

M = int(input())
N = int(input())
num_list = []

for i in range(M, N + 1):
    x = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                x += 1
                break
        if x == 0:
            num_list.append(i)

if len(num_list) < 1:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))