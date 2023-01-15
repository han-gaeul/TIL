# 숫자와 Z가 공백으로 구분되어 담긴 문자열이 주어진다
# 문자열에 있는 숫자를 차례대로 더하려고 한다
# 이 때 Z가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻이다
# 숫자와 Z로 이루어진 문자열 s가 주어질 때
# 머쓱이가 구한 값을 return

def solution(s):
    stack = []
    for num in s.split():
        try:
            stack.append(int(num))
        except:
            if stack:
                stack.pop()
    return sum(stack)