# 문자열 my_string이 매개변수로 주어진다
# my_string 안의 모든 자연수들의 합을 return

def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    answer = sum(answer)
    return answer