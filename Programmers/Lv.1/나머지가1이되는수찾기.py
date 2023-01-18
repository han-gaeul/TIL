# 자연수 n이 매개변수로 주어진다
# n을 x로 나눈 나머지가 1이 되도록하는 가장 작은 자연수 x를 return

def solution(n):
    return min([i for i in range(1, n) if n % i == 1])


# 더 효율적임
def solution(n):
    for i in range(1, n+1) :
        if n % i == 1 :
            return i