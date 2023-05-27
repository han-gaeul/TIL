# 정수 배열 arr와 2개의 구간이 담긴 배열 intervals가 주어진다
# intervals는 항상 [[a1, b1], [a2, b2]]의 꼴로 주어지며 각 구간은
# 닫힌 구간이다. 닫힌 구간은 양 끝값과 그 사이의 값을 모두 포함하는
# 구간을 의미한다. 이때 배열 arr의 첫번째 구간에 해당하는 배열과
# 두 번째 구간에 해당하는 배열을 앞뒤로 붙여 새로운 배열을
# 만들어 return

def solution(arr, intervals):
    first_interval = arr[intervals[0][0]:intervals[0][1] + 1]
    second_interval = arr[intervals[1][0]:intervals[1][1] + 1]
    return first_interval + second_interval