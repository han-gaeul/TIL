# 머쓱이는 친구들과 369 게임을 하고 있다
# 369 게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는
# 숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임이다
# 머쓱이가 말해야 하는 숫자 order가 매개변수로 주어질 때
# 머쓱이가 쳐야할 박수 횟수를 return

def solution(order):
    answer = 0
    for i in str(order):
        if i in ['3', '6', '9']:
            answer += 1
    return answer


def solution(order):
    answer = str(order).count('3') + str(order).count('6') + str(order).count('9')
    return answer