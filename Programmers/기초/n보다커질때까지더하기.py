# 정수 배열 numbers와 정수 n이 매개변수로 주어진다
# numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이
# n보다 커지는 순간 이때까지 더했던 원소들의 합을 return

def solution(numbers, n):
    total = 0
    for num in numbers:
        total += num
        if total > n:
            break
    return total