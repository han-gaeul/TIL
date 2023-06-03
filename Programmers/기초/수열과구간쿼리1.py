# 정수 배열 arr와 2차원 정수 배열 queries이 주어진다
# queries의 원소는 각각 하나의 query를 나타내며, [s, e] 꼴이다
# 각 query마다 순서대로 s <= i <= e인 모든 i에 대해 
# arr[i]에 1을 더한다
# 위 규칙에 따라 queries를 처리한 이후의 arr를 return

def solution(arr, queries):
    res = arr.copy()
    for query in queries:
        s, e = query
        for i in range(s, e + 1):
            res[i] += 1
    return res