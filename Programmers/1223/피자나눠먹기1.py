# 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라준다.
# 피자를 나눠먹을 사람의 수 n이 주어질때
# 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한
# 피자의 수를 return

def solution(n):
    if n % 7 == 0:
        answer = n // 7
    else:
        answer = n // 7 + 1
    return answer

# math 함수 활용
# ceil -> 실수를 올림하여 정수를 반환하는 함수
import math

def solution(n):
    return math.ceil(n//7)