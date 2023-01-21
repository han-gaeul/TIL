# 배열 arr가 주어진다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있다
# 이때 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 한다
# 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 한다
# 예를 들면 arr = [1, 1, 3, 3, 0, 1, 1]이면 [1, 3, 0, 1]을 return
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return

def solution(arr):
    answer = []
    # 다음에 올 원소와 비교하기 위해
    # arr에 있는 가장 첫 번째 원소를 추가
    answer.append(arr[0])

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])
    return answer