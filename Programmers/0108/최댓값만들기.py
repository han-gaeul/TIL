# 정수 배열 numbers가 매개변수로 주어진다.
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값 return

def solution(numbers):
    numbers.sort()
    a = numbers[0] * numbers[1]
    b = numbers[-1] * numbers[-2]
    if a > b:
        return a
    else:
        return b