# 두 정수 q, r과 문자열 code가 주어진다
# code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를
# 앞에서부터 순서대로 이어 붙인 문자열을 return

def solution(q, r, code):
    ans = ''
    for i in range(len(code)):
        if i % q == r:
            ans += code[i]
    return ans