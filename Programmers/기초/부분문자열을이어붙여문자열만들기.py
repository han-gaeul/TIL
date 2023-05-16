# 길이가 같은 문자열 배열 my_strings와 이차원 정수 배열
# parts가 매개변수로 주어진다
# parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터
# 인덱스 e까지의 부분 문자열을 의미한다.
# 각 my_strings의 원소의 parts에 해당하는 부분 문자열을
# 순서대로 이어 붙인 문자열을 return

def solution(my_strings, parts):
    ans = ''
    for i in range(len(my_strings)):
        string = my_strings[i]
        part = parts[i]
        substr = string[part[0]:part[1] + 1]
        ans += substr
    return ans