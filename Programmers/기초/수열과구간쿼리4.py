# 정수 배열 arr와 2차원 정수 배열 queries가 주어진다
# queries의 원소는 각각 하나의 query를 나타내며
# [s, e, k]꼴이다. 각 query마다 순서대로 s <= i <= e인
# 모든 i에 대해 i가 k의 배수이면 arr[i]에 1을 더한다
# 위 규칙에 따라 queries를 처리한 이후의 arr를 반환

def solution(arr, queries):
    for cur in queries:
        copy_arr = arr[:]
        to, from_, val = cur
        for elIdx in range(to, from_ + 1):
            if elIdx % val == 0:
                copy_arr[elIdx] += 1
        arr = copy_arr
    return arr