# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단
# n이 양의 정수 x의 제곱이라면 x + 1의 제곱을 return
# n이 양의 정수 x의 제곱이 아니라면 -1을 return

def solution(n):
    if int(n ** 0.5) == n ** 0.5:
        return ((n ** 0.5) + 1) ** 2
    else:
        return -1