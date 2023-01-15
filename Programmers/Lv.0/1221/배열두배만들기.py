# 정수 배열 numbers가 매개변수로 주어진다
# numbers의 각 원소에 두 배한 원소를 가진 배열을
# return 하도록 solution 함수 완성

def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(number * 2)
    return answer