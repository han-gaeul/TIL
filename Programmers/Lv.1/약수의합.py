# 정수 n을 입력받아 n의 약수를 모두 더한 값을 return

def solution(n):
    return sum([i for i in range(1, n + 1) if n % i == 0])