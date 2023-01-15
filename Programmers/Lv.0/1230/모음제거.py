# 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류한다
# 문자열 my_string이 매개변수로 주어질 때
# 모음을 제거한 문자열을 return

def solution(my_string):
    char = ['a', 'e', 'i', 'o', 'u']
    for c in char:
        my_string = my_string.replace(c, '')
    return my_string

def solution(my_string):
    return ''.join([i for i in my_string if not i in 'aeiou'])