# 5691

# 세 정수 A, B, C의 평균은 (A + B + C) / 3이다
# 세 정수의 중앙값은 수의 크기가 증가하는 순서로 정렬했을 때 가운데 있는 값이다
# 두 정수 A와 B가 주어진다. 이때 A, B, C의 평균과 중앙값을 같게 만드는
# 가장 작은 정수 C를 찾아라

# 입력은 여러 개의 테스트 케이스로 이루어져 있다
# 각 테스트 케이스는 한 줄로 이루어져 있고 A와 B가 주어진다
# 입력의 마지막 줄에는 0이 두 개 주어진다

# 각 테스트 케이스에 대한 정답을 한 줄에 하나씩 출력

while True:
    A, B = map(int, input().split())
    if (A, B) == (0, 0):
        break
    else:
        print(A - (B - A))


# C는 A보다 작으면서 B와 A의 차이값을 구해 A보다 차이값만큼 작으면 된다