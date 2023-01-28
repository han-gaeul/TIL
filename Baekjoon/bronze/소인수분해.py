# 11653

# 정수 N이 주어졌을 때 소인수분해하는 프로그램을 작성하라

# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력
# N이 1인 경우 아무것도 출력하지 않는다

N = int(input())

x = 2
while N != 1:
    if N % x == 0:
        print(x)
        N = N / x
    else:
        x += 1