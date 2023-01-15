# 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 함
# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 한다
# 삼각형의 세 변의 길이가 담긴 배열 sides가 매개변수로 주어진다
# 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2 return

def solution(sides):
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        return 1
    else:
        return 2



def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2