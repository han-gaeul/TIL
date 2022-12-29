# 정수가 담긴 배열 numbers와 문자열 direction이
# 매개변수로 주어진다. 배열 numbers의 원소를 
# direction 방향으로 한 칸씩 회전시킨 배열을 return

from collections import deque

def solution(numbers, direction):
    numbers_deque = deque(numbers)
    if direction == 'right':
        numbers_deque.rotate(1)
    elif direction == 'left':
        numbers_deque.rotate(-1)
    return list(numbers_deque)