# 양의 정수 n이 매개변수로 주어질 때
# n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 반환
# n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 반환

def solution(n):
    if n % 2 == 1:
        answer = range(1, n + 1, 2)
        return sum(answer)
    else:
        answer = range(2, n + 1, 2)
        ans = [x ** 2 for x in answer]
        return sum(ans)