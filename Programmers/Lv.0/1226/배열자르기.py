# 정수 배열 numbers와 정수 num1, num2가
# 매개변수로 주어질 때
# numbers의 num1번 째 인덱스부터
# num2번 째 인덱스까지 자른 정수 배열을 return

def solution(numbers, num1, num2):
    return numbers[num1:num2 + 1]