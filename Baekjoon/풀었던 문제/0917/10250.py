# 프로그램은 표준 입력에서 입력 데이터를 받는다
# T개의 테스트 데이터로 이루어져 있고 T는 입력의 맨 첫 줄에 주어진다
# 각 테스트 데이터는 한 행으로서 H, W, N 세 정수를 포함
# 각각 호텔의 층수, 각 층의 방 수, 몇 번째 손님인지 나타낸다

# 프로그램은 표준 출력에 출력한다
# 각 테스트 데이터마다 정확히 한 행을 출력
# 내용은 N번째 손님에게 배정되어야 하는 방 번호 출력

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    room = N // H + 1

    if floor == 0:
        room -= 1
        floor = H

    print(floor * 100 + room)


# 손님은 층수에 상관없이 엘리베이터에서 가장 가까운 방 선호
# 그러면 N번째 손님은 몇호에 배정 되는냐? 가 문제
# 손님이 들어올 때 101호, 102호, 103, ... 들어간다
# 그렇다면 높이가 5일 때 6번째 손님은 102호에 들어간다
# 여기서 찾을 수 있는 규칙은 손님이 들어가는 층수는
# 몇 번째 손님을 높이로 나눈 나머지이다.
# 손님이 들어가는 룸 번호는 몇 번째 손님을 높이로 나눈 몫의 + 1
# H = 5, W = 5, N = 6 이라고 할 때 층수는 6 % 5 = 1층
# 룸 번호는 6 / 5 + 1 = 2호, 따라서 102호가 된다
# 예외가 하나 발생하는데 높이가 맞아 떨어질 때이다
# N이 5라고 하면 층수는 5 % 5= 0층
# 룸 번호 5 / 5 + 1 = 2호 따라서 0층에 2호가 되는데
# 층이 0층이라면 높이를 H로 설정해준다
# 그리고 룸 번호를 하나 줄여주는 과정을 추가한다
# 그렇다면 최종적으로 배정되는 방은 501호 된다