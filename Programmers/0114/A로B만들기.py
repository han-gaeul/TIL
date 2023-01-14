# 문자열 before와 after가 매개변수로 주어질 때
# before의 순서를 바꾸어 after를 만들 수 있으면 1을,
# 만들 수 없으면 0을 return

def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0