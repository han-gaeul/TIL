# 머쓱이는 RPG 게임을하고 있다
# 게임에는 up, down, left, right 방향키가 있으며
# 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동한다
# 예를 들어 [0, 0]에서 up 버튼을 누르면 캐릭터의 좌표는 [0, 1]
# down을 누르면 [0, -1], left를 누르면 [-1, 0]
# right를 누르면 [1, 0]이다
# 머쓱이가 입력한 방향키의 배열 keyinput과
# 맵의 크기 board가 매개변수로 주어진다.
# 캐릭터는 항상 [0, 0]에서 시작할 때 키 입력이 모두
# 끝난 뒤에 캐릭터의 좌표 [x, y]를 return
# [0, 0]은 board의 정중앙에 위치한다
# board의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지
# 오른쪽으로 최대 [4, 0]까지 이동

def solution(keyinput, board):
    limit_x = (board[0] -1) // 2
    limit_y = (board[1] -1) // 2
    commands = {
        'up' : [0, 1],
        'down' : [0, -1],
        'left' : [-1, 0],
        'right' : [1, 0],
    }
    x = y = 0
    for command in keyinput:
        dx, dy = commands[command]
        nx, ny = x + dx, y + dy
        if abs(nx) <= limit_x and abs(ny) <= limit_y:
            x, y = nx, ny
    return [x, y]