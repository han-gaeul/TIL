# 정수 배열 arr와 2차원 정수 배열 queries가 주어진다
# queries의 원소는 각각 하나의 query를 나타내며
# [i, j]꼴이다. 각 query마다 순서대로 arr[i]의 값과 arr[j]의
# 값을 서로 바꾼다. 위 규칙에 따라 queries를 처리한 이후의
# arr를 반환

def solution(arr, queries):
    for query in queries:
        i, j = query
        arr[i], arr[j] = arr[j], arr[i]
    return arr