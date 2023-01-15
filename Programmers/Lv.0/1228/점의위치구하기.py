# 사분면은 한 평면을 x축과 y축을 기준으로 나눈 네 부분이다
# 사분면은 아래와 같이 1부터 4까지 번호를 매긴다
# x 좌표와 y 좌표가 모두 양수면 제1사분면
# x 좌표가 음수, y 좌표가 양수이면 제2사분면
# x 좌표와 y 좌표가 모두 음수면 제3사분면
# x 좌표가 양수, y 좌표가 음수면 제4사분면
# x 좌표 (x, y)를 차례대로 담은 정수 배열 dot이 매개변수로 주어진다
# 좌표 dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return

def solution(dot):
    x, y = dot[0], dot[1]
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4