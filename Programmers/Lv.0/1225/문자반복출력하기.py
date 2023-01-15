# 문자열 my_string과 정수 n이 매개변수로 주어질 때
# my_string에 들어있는 각 문자를 n만큼 반복한 문자열 return

def solution(my_string, n):
    answer = []
    for i in my_string:
        answer.append(i * n)
    return ''.join(answer)


def solution(my_string, n):
    return ''.join(i * n for i in my_string)