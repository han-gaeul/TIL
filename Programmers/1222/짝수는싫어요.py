# 정수 n이 매개변수로 주어질 때
# n 이하의 홀수가 오름차순으로 담긴 배열을 return

def solution(n: int) -> list:
    return [x for x in range(1, n + 1) if x % 2 == 1]