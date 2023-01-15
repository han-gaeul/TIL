# 정수 n이 매개변수로 주어질 때
# n의 각 자리 숫자의 합을 return

def solution(n):
    result = 0
    for i in str(n):
        result += int(i)
    return result


def solution(n):
    return sum([int(i) for i in str(n)])


def solution(n):
    answer = list(map(int, str(n)))
    return sum(answer)