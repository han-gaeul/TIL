# 1037

# 양수 A가 N의 진짜 약수가 되려면 N이 A의 배수이고 A가 1과 N이 아니어야 한다
# 어떤 수 N의 진짜 약수가 모두 주어질 때 N을 구하라

# 첫째 줄에 N의 진짜 약수의 개수가 주어진다
# 둘째 줄에 N의 진짜 약수가 주어진다
# 2보다 크거나 같은 자연수이고 중복되지 않는다

# 첫째 줄에 N을 출력

N = int(input())
nums = list(map(int, input().split()))
print(min(nums) * max(nums))