# 소인수분해란 어떤 수를 소수들의 곱으로 표현한 것
# 예를 들어 12를 소인수 분해하면 2 * 2 * 3으로 나타낼 수 있다
# 따라서 12의 소인수는 2와 3이다
# 자연수 n이 매개변수로 주어질 때 n의 소인수를
# 오름차순으로 담은 배열을 return

def solution(n):
    prime_factor = []
    answer = []
    i = 2
    while i <= n:
        if n % i == 0:
            prime_factor.append(i)
            n = n // i
        else:
            i += 1
    for i in prime_factor:
        if i not in answer:
            answer.append(i)
    return answer