# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어진다
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return

def solution(numbers):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = list(set(num) - set(numbers))
    return sum(x)


def solution(numbers):
    return 45 - sum(numbers)