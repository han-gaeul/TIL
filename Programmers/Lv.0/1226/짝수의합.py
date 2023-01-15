# 정수 n이 주어질 때 n 이하의 짝수를 모두 더한 값을 return

def solution(n):
    result = 0
    for num in range(1, n + 1):
        if num % 2 == 0:
            result += num
    return result