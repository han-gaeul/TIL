# 문자열 배열 strlist가 매개변수로 주어진다
# strlist 각 원소의 길이를 담은 배열 return

def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer


def solution(strlist):
    return [len(i) for i in strlist]