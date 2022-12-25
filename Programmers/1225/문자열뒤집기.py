# 문자열 my_string이 매개변수로 주어진다
# my_string을 거꾸로 뒤집은 문자열을 return

# reverse
def solution(my_string):
    return ''.join(reversed(my_string))

# 슬라이싱
def solution(my_string):
    return my_string[::-1]