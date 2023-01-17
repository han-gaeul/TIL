# N개의 숫자가 공백 없이 쓰여있다
# 이 숫자를 모두 합해서 출력

# 첫째 줄에 숫자의 개수 N이 주어진다
# 둘째 줄에 숫자 N개가 공백없이 주어진다

# 입력으로 주어진 숫자 N개의 합을 출력

N = input()
print(sum(map(int,input())))

#! --------------------------------

N = input()
nums = input()
result = 0

for i in nums:
    result += int(i)
print(result)

#! --------------------------------

N = input()
nums = input()
result = 0

for i in range(N):
    result += int(nums[i])
print(result)