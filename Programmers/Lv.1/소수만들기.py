# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구한다
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때
# 소수가 되는 경우의 개수를 return

from itertools import combinations

def solution(nums):
    answer = 0
    # nums에서 3개의 수를 선택
    for i in combinations(nums, 3):
        # 선택한 수를 합하고 s에 저장
        s = sum(i)
        # s가 소수인지 판별하는 변수 선언
        check = True
        # 2부터 s의 제곱근까지 반복
        for j in range(2, int(s ** 0.5) + 1):
            if s % j == 0:
                check = False
                break
        if check is True:
            answer += 1
    return answer