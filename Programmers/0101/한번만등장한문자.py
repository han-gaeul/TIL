# 문자열 s가 매개변수로 주어진다
# s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return
# 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return

def solution(s):
    answer = ''
    s = sorted(s)
    for i in s:
        if s.count(i) == 1:
            answer += i
    return answer