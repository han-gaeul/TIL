# array의 각 element 중 divisor로 나누어 떨어지는 값을
# 오름차순으로 정렬한 배열을 return
# divisor로 나누어 떨어지는 element가 하나도 없다면 -1 return

def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]