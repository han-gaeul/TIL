# 문자열 my_string이 매개변수로 주어진다
# my_string에서 중복된 문자를 제거하고
# 하나의 문자만 남긴 문자열을 return

def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer


def solution(my_string):
    return ''.join(dict.fromkeys(my_string))