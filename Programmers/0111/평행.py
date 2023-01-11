# 점 네 개의 좌표를 담은 이차원 배열 dots가 다음과 같이 주어진다
# [[x1, y2], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때
# 두 직선이 평행이 되는 경우가 있으면 1, 없으면 0을 return

def solution(dots):
    # 점 4개를 두 쌍으로 나누어 각 쌍에 대한 기울기를 구함
    # 기울기 : (y2 - y1) / (x2 - x1)
    slope1 = (dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
    slope2 = (dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0])
    slope3 = (dots[3][1] - dots[0][1]) / (dots[3][0] - dots[0][0])
    slope4 = (dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
    
    # 기울기를 비교해 평행 여부 판별
    if slope1 == slope2 or slope3 == slope4:
        return 1
    else:
        return 0