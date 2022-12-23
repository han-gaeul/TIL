# 정수 배열 numbers가 매개변수로 주어진다
# numbers의 원소의 평균값을 return

# 1. sum, len 활용
def solution(numbers):
    medium = sum(numbers) / len(numbers)
    return medium


# 2. for문 활용
def solution(numbers):
    sum = 0
    for num in numbers:
        sum += num
    medium = sum / len(numbers)
    return medium


# 3. 함수 활용
import statistics
def solution(numbers):
    medium = statistics.mean(numbers)
    return medium

import numpy
def solution(numbers):
    medium = numpy.mean(numbers)
    return medium