# 문자열 my_string, overwite_string과 정수 s가 주어진다
# 문자열 my_string의 인덱스 s부터 overwite_string의 
# 길이만큼 문자열 overwrite_string으로 바꾼 문자열을 return

def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]