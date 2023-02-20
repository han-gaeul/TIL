# 4493

# 가위 바위 보는 두 명이서 하는 게임이다
# 보통 미리 정해놓은 수만큼 게임을 하고 많은 게임을 이긴 사람이 최종 승자가 된다
# 가위 바위보를 한 횟수와 매번 두 명이 무엇을 냈는지가 주어졌을 때
# 최종 승자를 출력하라
# 바위는 가위를 이긴다
# 가위는 보를 이긴다
# 보는 바위를 이긴다

# 첫째 줄에 테스트 케이스의 개수 t가 주어진다
# 각 테스트 케이스의 첫째 줄에는 가위 바위 보를 한 횟수 n이 주어진다
# 다음 n개의 줄에는 R, P, S가 공백으로 구분되어 주어진다
# R, P, S는 순서대로 바위, 보, 가위이고 첫 번째 문자는 Player 1의 선택,
# 두 번째 문자는 Player 2의 선택이다

# 각 테스트 케이스에 대해서 승자를 출력
# 만약 비겼을 경우 TIE를 출력



# 1.
for _ in range(int(input())):
    p1 = p2 = 0
    for i in range(int(input())):
        x, y = input().split()
        if x == y:
            continue
        elif (x == 'R' and y == 'S') or (x == 'P' and y == 'R') or (x == 'S' and y == 'P'):
            p1 += 1
        else:
            p2 += 1
    if p1 > p2:
        print('Player 1')
    elif p1 < p2:
        print('Player 2')
    else:
        print('TIE')
# 2396ms


# 2.
# 각 옵션이 이길 수 있는 옵션을 미리 계산
winning_options = {'R': 'S', 'P': 'R', 'S': 'P'}
for _ in range(int(input())):
    p1 = p2 = 0
    n = int(input())
    for i in range(n):
        x, y = input().split()
        if x == y:
            continue
        elif y == winning_options[x]:
            p1 += 1
        else:
            p2 += 1
    if p1 > p2:
        print('Player 1')
    elif p1 < p2:
        print('Player 2')
    else:
        print('TIE')
# 1984ms -> 2104ms
# range 함수에 인자로 변수 대신 input 함수를 넣으면 시간이 늘어남