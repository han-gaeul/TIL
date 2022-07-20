import sys

sys.stdin = open("1284.txt", "r")

# P : A 수도 1리터당 요금
# Q : B 수도 기본 요금
# R : B 수도 한 달 사용량
# S : B 수도 초과 사용량에 대해 1리터당 요금
# W : 내가 쓴 한 달 사용량

T = int(input())

for i in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    # A 수도는 내가 쓴만큼 가격이 오르기 때문에
    # 요금 * 내가 쓴 사용량
    Asudo = P * W
    Bsudo = 0

    # B 수도는 기본양이 제공 되고
    # 기본양보다 많이 사용하면 추가요금 발생
    if W < R:
        Bsudo = Q
    else:
        Bsudo = Q + (W - R) * S

    if Asudo < Bsudo:
        print('#{} {}'.format(i, Asudo))
    else:
        print('#{} {}'.format(i, Bsudo))