# 배열을 정렬하는 것은 쉽다
# 수가 주어지면 그 수의 각 자리수를 내림차순으로 정렬해보자

# 첫째 줄에 정렬하려고 하는 수 N이 주어진다

# 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력

N = int(input())
nums = list(map(int, str(N)))

nums.sort(reverse=True)

for i in nums:
    print(i, end = '')