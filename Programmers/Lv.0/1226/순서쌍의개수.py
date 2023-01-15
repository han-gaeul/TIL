# 순서쌍이란 두 개의 숫자를 순서를 정하여
# 짝지어 나타낸 쌍으로 (a, b)로 표기
# 자연수 n이 매개변수로 주어질 때
# 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return

def solution(n):
    answer = []
    for i in range(1, n + 1):
        if n % i == 0:
            answer.extend([(i, n // i)])
    return len(answer)


def solution(n):
    return len([number for number in range(1, n + 1) if n % number == 0])


def solution(n):
    return len(list(filter(lambda v : n % (v + 1) == 0, range(n))))