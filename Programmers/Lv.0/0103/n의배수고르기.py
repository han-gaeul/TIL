# 정수 n과 정수 배열 numlist가 매개변수로 주어질 때
# numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return

def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n ==0:
            answer.append(i)
    return answer


def solution(n, numlist):
    return ([i for i in numlist if i % n == 0])


def solution(n, numlist):
    return list(filter(lambda x : x % n == 0, numlist))