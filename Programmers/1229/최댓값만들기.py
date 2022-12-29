# 정수 배열 numbes가 매개변수로 주어진다
# numbers의 원소 중 두 개를 곱해 만들 수 있는
# 최댓값을 return

def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]