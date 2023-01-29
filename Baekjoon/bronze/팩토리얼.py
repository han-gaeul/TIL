# 10872

# 0보다 크거나 같은 정수 N이 주어진다
# 이때 N!을 출력



# for문
N = int(input())
result = 1
if N > 0:
    for i in range(1, N + 1):
        result *= i
print(result)


# 재귀 함수
def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N - 1)
N = int(input())
print(factorial(N))



# 팩토리얼은 1부터 n까지 양의 정수를 모두 곱한 수
# 0! = 1로 가정하고 n! = n * (n - 1)!의 성질을 가짐

# 재귀 함수는 자기 자신을 호출하는 함수