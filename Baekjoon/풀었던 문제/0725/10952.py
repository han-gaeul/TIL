# A + B - 5
# 두 정수 A와 B를 입력받은 다음
# A + B를 출력

while 1:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        print(A + B)

# while문을 True로 두어 계속 반복되게 함
# 숫자를 입력 받고 if문을 이용해서
# while문을 돌 때마다 입력되는 정수 2개를 더한 값 출력
# 0이 입력 됐을 때는 멈추게 함
