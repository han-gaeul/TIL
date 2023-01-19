# 두 정수 left와 right가 매개변수로 주어진다
# left부터 right까지의 모든 수들 중에서 약수의 개수가
# 짝수인 수는 더하고 약수의 개수가 홀수인 수는 뺸 수를 return

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
    return answer