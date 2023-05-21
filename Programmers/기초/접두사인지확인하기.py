# 어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미한다
# 예를 들어, 'banana'의 모든 접두사는 'b', 'ba', 'ban', 'bana',
# 'banan', 'banana'이다.
# 문자열 my_strign과 is_predix가 주어질 때, is_prefix가
# my_string의 접두사라면 1을, 아니면 0을 return

def solution(my_string, is_prefix):
    n, m = len(my_string), len(is_prefix)
    if m > n:
        return 0
    elif m == n:
        if my_string == is_prefix:
            return 1
        else:
            return 0
    for i in range(m):
        if my_string[i] != is_prefix[i]:
            return 0
    return 1