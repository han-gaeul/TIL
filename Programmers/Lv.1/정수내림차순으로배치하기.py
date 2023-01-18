# 정수 n을 매개변수로 입력받고 n의 각 자릿수를
# 큰 것부터 작은 순으로 정렬한 새로운 정수를 return
# 예를 들어 n이 118372이면 873211 return

def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))