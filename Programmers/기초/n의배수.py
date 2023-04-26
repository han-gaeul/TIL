# 정수 num과 n이 매개변수로 주어질때 num이 n의 배수이면
# 1을 반환, n의 배수가 아니라면 0을 반환

def solution(num, n):
    if num % n == 0:
        return 1
    else:
        return 0