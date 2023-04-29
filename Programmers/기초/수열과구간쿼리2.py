# 정수 배열 arr와 2차원 정수 배열 queries가 주어진다
# queries의 원소는 각각 하나의 query를 나타내며
# [s, e, k] 꼴이다. 각 query마다 순서대로 s <= i <= e인
# 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾는다
# 각 쿼리의 순서에 맞게 답을 저장한 배열을 반환
# 단, 특정 쿼리의 답이 존재하지 않으면 -1 반환

def solution(arr, queries):
    ans = []
    for s, e, k in queries:
        tmp = sorted(arr[s:e+1])
        res = next((x for x in tmp if x > k), -1)
        ans.append(res)
    return ans