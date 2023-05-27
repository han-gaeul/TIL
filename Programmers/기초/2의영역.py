# 정수 배열 arr가 주어진다
# 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return
# 단, arr에 2가 없는 경우 [-1] return

def solution(arr):
    if 2 not in arr:
        return [-1]
    start = arr.index(2)
    end = len(arr) - arr[::-1].index(2) - 1
    return arr[start:end + 1] if start <= end else [-1]