# 선분 세 개로 삼각형을 만들기 위해서 다음과 같은 조건을 만족해야 한다
# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 한다
# 삼각형의 두 변의 길이가 담긴 배열 sides가 매개변수로 주어진다
# 나머지 한 변이 될 수 있는 정수의 개수를 return

def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1

# -1은 '가장 큰 변의 길이 = 나머지 두 변의 길이의 합'을 제거