# 9085

# 10보다 작거나 같은 자연수 N개를 주면 합을 구하라

# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다
# 각 테스트 케이스는 첫 줄에 자연수의 개수 N이 주어지고
# 그 다음 줄에는 N개의 자연수가 주어진다. 각각의 자연수 사이에는 하나씩의 공백이 있다

# 각 테스트 케이스에 대해서 주어진 자연수의 합을 한 줄에 하나씩 출력

T = int(input())
for _ in range(T):
    nums = []
    N = int(input())
    nums = sum(list(map(int, input().split())))
    print(nums)