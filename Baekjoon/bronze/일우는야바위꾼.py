# 20361

# 전설의 야바위꾼 일우는 Shell Game으로 야바위를 한다. Shell Game은 다음과 같은 절차로 진행된다
# 1. 진행자가 N개의 컵을 일렬로 놓고 그 중 X번째 컵에 공을 숨긴다
# 2. 임의의 서로 다른 두 컵의 위치를 맞바꾼다. 이 항목을 K번 수행한다
# 만약 공을 숨겨둔 컵을 움직인다면 공도 그 컵을 따라서 움직인다
# 3. 참가자는 몇 번째 컵에 공이 숨겨져 있는지 추측한다
# 4. 그 컵에 공이 숨겨져 있다면 참가자가 그렇지 않다면 진행자가 이긴다
# 수혁이는 Shell Game을 잘하고 싶다. 하지만 일우가 진행자라면 무슨 수를 써도 이길 수 없어
# 수혁이는 일우의 사기도박을 의심하고 있다.
# 현재 우리는 수혁과 일우가 진행한 Shell Game의 모든 기록을 입수했다
# 이를 바탕으로 일우가 사기도박을 하지 않았다면 공이 몇 번째 컵에 있는지 알려주자

# 첫째 줄에 N, X가 공백으로 구분되어 주어진다
# 둘째 줄부터 K개의 줄에는 순서대로 바꾼 두 컵의 위치 Ai, Bi가 공백으로 구분되어 주어진다

# 일우가 사기도박을 하지 않았다면 공이 몇 번째 위치의 컵에 있어야 하는지 정수로 출력

N, X, K = map(int, input().split())
# 각 컵의 위치를 나타내는 리스트 생성
cup = [0] * (N + 1)
# 공이 있는 컵의 위치를 1로,
# 그 외의 컵은 0으로 초기화
cup[X] = 1
for i in range(K):
    A, B = map(int, input().split())
    # 두 컵의 위치를 서로 바꾼다
    check = cup[A]
    cup[A] = cup[B]
    cup[B] = check
# 1이 위치한 인덱스 출력
print(cup.index(1))