# 문자열 my_string과 정수 n이 매개변수로 주어질 때
# my_string의 뒤의 n글자로 이루어진 문자열을 return

def solution(my_string, n):
    my_string = list(my_string)
    ans = my_string[-n:]
    return ''.join(ans)