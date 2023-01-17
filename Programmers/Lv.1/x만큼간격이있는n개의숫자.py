# 정수 x와 자연수 n을 입력 받아 x부터 시작해
# x씩 증가하는 숫자를 n개 지니는 리스트를 return

def solution(x, n):
    return [i * x + x for i in range(n)]