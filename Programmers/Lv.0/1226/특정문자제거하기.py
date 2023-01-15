# 문자열 my_string과 문자 letter이 매개변수로 주어진다
# my_string에서 letter를 제거한 문자열을 return

def solution(my_string, letter):
    return ''.join([x for x in my_string if x != letter])