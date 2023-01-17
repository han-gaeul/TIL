# 대문자와 소문자가 섞여있는 문자열 s가 주어진다
# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True
# 다르면 False를 return
# 'p', 'y' 모두 하나도 없는 경우는 항상 True를 return
# 단, 개수를 비교할 때 대문자와 소문자를 구별하지 않는다
# 예를 들어 s가 "pPoooyY"면 True return
# "Pyy"라면 False return

def solution(s):
    p = 0
    y = 0
    for i in s:
        if i == 'p' or i == 'P':
            p += 1
        elif i == 'y' or i == 'Y':
            y += 1
    
    if p == y:
        return True
    else:
        return False



def solution(s):
    return s.lower().count('p') == s.lower().count('y')