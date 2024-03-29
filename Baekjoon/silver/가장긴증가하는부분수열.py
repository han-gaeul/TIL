# 11053

# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하라
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50}인 경우에
# 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50}이고
# 길이는 4이다

# 첫째 줄에 수열 A의 크기 N이 주어진다
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다

# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력

N = int(input())
arr = list(map(int, input().split()))
# 모든 원소의 길이는 자기 자신만으로 1이 됨
dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))



# 초기값으로 모든 원소를 1로 초기화한다
# 왜냐하면 자기 자신만으로도 길이가 1인 부분 수열이 되기 때문
# 그리고 1부터 i - 1까지의 위치에서 i번째 원소보다
# 작은 수를 찾아 해당 위치에서의 부분 수열의 길이에
# 1을 더한 값과 현대 위치에서의 부분 수열의 길이 중
# 큰 값을 선택해 dp[i]에 저장한다.