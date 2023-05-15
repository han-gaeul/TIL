# 문자열 my_string과 정수 배열 index_list가 매개변수로 주어진다
# my_string의 index_list의 원소들에 해당하는 인덱스의
# 글자들을 순서대로 이어붙인 문자열을 return

def solution(my_string, index_list):
    ans = ''
    for i in index_list:
        ans += my_string[i]
    return ans