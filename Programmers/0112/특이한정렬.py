# 정수 n을 기준으로 n과 가까운 수부터 정렬하려고 한다
# 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치
# 정수가 담긴 배열 numlist와 정수 n이 주어질 때
# numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열 return

def solution(numlist, n):
    return sorted(numlist, key = lambda x: (abs(x - n), -x))

# numlist 인자를 입력받아 각 요소 x와 n 값의 절대값 차이와
# -x를 기준으로 정렬
# 각 요소 x와 n 값의 절대값의 차이를 기준으로 정렬하고
# 같은 경우 -x를 기준으로 정렬하여 정렬된 numlist 반환
# 각 요소들이 n에서 가까운 것부터 멀리 떨어져 있는 것
# 순서대로 정렬되고 거리가 같은 경우 내림차순으로 정렬