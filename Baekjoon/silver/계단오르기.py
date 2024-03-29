# 2579

# 계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한
# 도착점까지 가는 게임이다. 각각의 계단에는 일정한 점수가 쓰여 있는데
# 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다
# 예를 들어, 시작점에서부터 첫번째, 두번째, 네번째, 여섯번째
# 계단을 밟아 도착점에 도달하면 총 점수는 10 + 20 + 25 + 20
# = 75점이 된다. 계단 오르는 데는 다음과 같은 규칙이 있다
# 1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다
# 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로
# 오를 수 있다.
# 2. 연속된 세 개의 계단을 모두 밟아서는 안 된다.
# 단, 시작점은 계단에 포함되지 않는다
# 3. 마지막 도착 계단은 반드시 밟아야 한다
# 따라서 첫번째 계단을 밟고 이어 두번째 계단이나, 세번째 계단으로
# 오를 수 있다. 하지만, 첫번째 계단을 밟고 이어 네번째 계단으로
# 올라가거나, 첫번째, 두번째, 세번째 계단을 연속해서 모두 밟을 수는 없다
# 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는
# 총 점수의 최댓값을 구하라

# 입력의 첫째 줄에 계단의 개수가 주어진다
# 둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 
# 각 계단에 쓰여 있는 점수가 주어진다

# 첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값 출력

n = int(input())
# 계단의 점수 입력 받을 리스트 초기화
stair = [0] * 301
for i in range(n):
    stair[i] = int(input())
# d[i] : i번째 계단까지 갔을 때 얻을 수 있는 최대 점수
d = [0] * 301
# 첫번째 계단은 그대로 밟는 경우
d[0] = stair[0]
# 두번째 계단은 첫번째 계단을 밟고 오르는 경우
d[1] = stair[0] + stair[1]
# 세번째 계단은 두가지 경우 중 큰 값
d[2] = max(stair[0] + stair[2], stair[1] + stair[2])
# 다이나믹 프로그래밍
for i in range(3, n):
    d[i] = max(d[i - 3] + stair[i - 1] + stair[i], d[i - 2] + stair[i])
print(d[n - 1])

# 문제에서는 한 번에 연속된 세 개의 계단은 밟을 수 없다는
# 제약 조건이 있으므로 현재 계단에서 오를 수 있는 경우는
# 이전 계단에서 바로 오르거나, 이전 계단에서 한 계단을
# 뛰어넘고 오르는 두 가지 경우가 있다.
# d[i]는 i번째 계단까지 갔을 때 얻을 수 있는 최대 점수를 의미한다
# 따라서 d[i]는 다음과 같이 구할 수 있다
# 1. i -1번째 계단에서 오른 경우 : d[i - 1] + stair[i]
# 2. i - 2번째 계단에서 한 칸을 뛰어넘고 올라온 경우 :
# d[i - 2] + stair[i]
# 이때, 연속된 세 개의 계단을 밟을 수 없다는 조건을 고려해
# i - 3번째 계단에서 두 칸을 뛰어넘고 올라오는 경우는
# i - 1번째 계단에서 바로 올라오는 경우와 겹치기 때문에 제외한다.
# 이를 모든 계단에 대해 반복하면, d[n - 1]에는 n번째 계단까지
# 올랐을 때 얻을 수 있는 최대 점수가 저장된다