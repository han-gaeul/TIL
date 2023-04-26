# 정수 number와 n, m이 주어진다
# number가 n의 배수이면서 m의 배수이면 1을,
# 아니라면 0을 반환

def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0