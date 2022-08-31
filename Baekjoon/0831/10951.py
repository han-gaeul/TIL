# 각 테스트 케이스마다 두 정수 A와 B를 입력 받은 다음 A + B를 출력

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break