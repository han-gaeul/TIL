# 정수를 저장한 배열 arr에서 가장 작은 수를 제거한 배열을 return
# 단, 반환하려는 배열이 빈 배열인 경우 -1 return
# 예를 들어 arr이 [4, 3, 2, 1]인 경우 [4, 3, 2] return
# [10]이면 [-1] return

def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        answer = arr
        answer.remove(min(arr))
        return answer