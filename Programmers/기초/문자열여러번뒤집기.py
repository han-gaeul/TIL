# 문자열 my_string과 이차원 정수 배열 queries가 
# 매개변수로 주어진다. queries의 원소는 [s, e] 형태로,
# my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미이다
# my_string에 queries의 명령을 순서대로 처리한 후의
# 문자열을 return

def solution(my_string, queries):
    my_string = list(my_string)
    for query in queries:
        start, end = query
        my_string[start:end + 1] = reversed(my_string[start:end + 1])
    return ''.join(my_string)