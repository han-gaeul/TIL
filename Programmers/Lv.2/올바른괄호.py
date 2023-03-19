# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면
# 반드시 ')' 문자로 닫혀야 한다는 뜻이다
# 예를 들어, '()()' 또는 '(())()'는 올바른 괄호이다
# ')()(' 또는 '(()('는 올바르지 않은 괄호이다
# '(' 또는 ')'로만 이루어진 문자열 s가 주어졌을 때
# 문자열 s가 올바른 괄호이면 true를 return
# 올바르지 않은 괄호이면 false를 return

def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            # 스택이 비어있다면
            if not stack:
                return False
            # 스택이 비어있지 않다면
            stack.pop()
    # 모든 문자열을 다 읽었을 때
    # 스택이 비어있다면
    if not stack:
        return True
    else:
        return False