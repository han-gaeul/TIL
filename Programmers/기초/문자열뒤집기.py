# 문자열 my_string과 정수 s, e가 매개변수로 주어질 때
# my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return

def solution(my_string, s, e):
    my_string = list(my_string)
    rev_str = my_string[s:e + 1][::-1]
    my_string[s:e + 1] = rev_str
    return ''.join(my_string)