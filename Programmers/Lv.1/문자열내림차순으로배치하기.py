# 문자열 s에 나타나는 문자를 큰 것부터 작은 순으로 정렬해
# 새로운 문자열을 return
# s는 영문 대소문자로만 구성되어 있으며
# 대문자는 소문자보다 작은 것으로 간주

def solution(s):
    return (''.join(reversed(sorted(s))))


def solution(s):
    return (''.join(sorted(s)[::-1]))