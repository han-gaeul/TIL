a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

# 논리적으로 한 단위로 처리해야 하는 경우 콜론을 찍고 들여쓰기로 작성
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)
