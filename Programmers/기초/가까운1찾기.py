# 정수 배열 arr가 주어진다. 이때 arr의 원소는 1 또는 0이다
# 정수 idx가 주어졌을 때, idx 보다 크면서 배열의 값이 1인
# 가장 작은 인덱스를 찾아서 return
# 단, 만약 그러한 인덱스가 없다면 -1 return

def solution(arr, idx):
    for i in range(idx, len(arr)):
        cur = arr[i]
        if cur == 1:
            return i
    return -1