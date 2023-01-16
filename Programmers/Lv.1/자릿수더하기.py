# 자연수 N이 주어지면 N의 각 자릿수의 합을 구해서 return
# 예를 들어 N = 123이면 1 + 2 + 3 = 6 return

def solution(N):
    return sum([int(i) for i in str(N)])