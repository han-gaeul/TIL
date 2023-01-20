# 새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이지 않는다
# 이 놀이기구의 원래 이용료는 price원인데 놀이기구를
# N번 째 이용한다면 원래 이용료의 N배를 받기로 했다
# 처음 이용료가 100원이었다면 2번째에는 200원,
# 3번째에는 300원으로 요금이 인상된다
# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는
# 금액에서 얼마가 모자라는지 return
# 단, 금액이 부족하지 않으면 0을 return

def solution(price, money, count):
    for i in range(1, count + 1):
        money -= price * i
    if money < 0:
        return abs(money)
    else:
        money = 0
    return money