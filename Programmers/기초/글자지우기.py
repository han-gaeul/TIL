# 문자열 my_string과 정수 배열 indices가 주어질 때
# my_string에서 indies의 원소에 해당하는 인덱스의 글자를
# 지우고 이어붙인 문자열을 return

def solution(my_string, indices):
    str_list = list(my_string)
    for idx in sorted(indices, reverse=True):
        del str_list[idx]
    return ''.join(str_list)