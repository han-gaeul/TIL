# 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있다
# str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를
# '(최소값) (최대값)' 형태의 문자열을 return
# 예를 들어 s '1 2 3 4'라면 '1 4'를 반환하고
# '-1 -2 -3 -4'라면 '-4 -1'을 반환

def solution(s):
    numbers = list(map(int, s.split()))
    min_num = min(numbers)
    max_num = max(numbers)
    return f'{min_num} {max_num}'