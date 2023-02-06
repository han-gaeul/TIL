# 10817

# 세 정수 A, B, C가 주어진다. 이떄 두 번째로 큰 정수를 출력

# 첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다

# 두 번째로 큰 정수를 출력

nums = list(map(int, input().split()))
nums.sort()
print(nums[1])