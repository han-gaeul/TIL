# 정수 n과 문자열 control이 주어진다
# control은 w, a, s, d의 4개의 문자로 이루어져 있으며
# control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꾼다
# w : n이 1 커진다
# s : n이 1 작아진다
# d : n이 10 커진다
# a : n이 10 작아진다
# 위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는
# n의 값을 반환

def solution(n, control):
    for i in control:
        if i == 'w':
            n += 1
        elif i == 's':
            n -= 1
        elif i == 'd':
            n += 10
        elif i == 'a':
            n -= 10
    return n