# 6359

# 서강대학교 곤자가 기숙사의 지하에는 n개의 방이 일렬로 늘어선 감옥이 있다
# 각 방에는 벌점을 많이 받은 학생이 구금되어있다
# 그러던 어느날 감옥 간수인 상범이는 지루한 나머지 정신나간 게임을 하기로 했다
# 게임의 첫번째 라운드에서 상범이는 위스키를 한 잔 들이키고 달려가며 감옥을 한 개씩 모두 연다
# 그 다음 라운드에서는 2, 4, 6, ... 번 방을 다시 잠그고
# 세번째 라운드에서는 3, 6, 8, ... 번 방이 열려있으면 잠그고, 잠겨있으면 연다
# k번째 라운드에서는 번호가 k의 배수인 방이 열려있으면 잠그고, 잠겨있으면 연다
# 이렇게 n번째 라운드까지 진행한 이후 상범이는 위스키의 마지막 병을 마시고 쓰러져 잠든다
# 구금되어있는 몇 명(어쩌면 0명)의 학생들은 자신의 방을 잠그지 않은채
# 상범이가 쓰러져 버렸단 것을 깨닫고 즉시 도망친다
# 방의 개수가 주어졌을 때 몇 명의 학생이 도주할 수 있는지 알아보자

# 입력의 첫 번째 줄에는 테스트 케이스의 개수 T가 주어진다
# 각 테스트 케이스는 한 줄에 한 개씩 방의 개수 n이 주어진다

# 한 줄에 한 개씩 각 테스트 케이스의 답,
# 즉 몇 명이 탈출할 수 있는지 출력



# 1.
T = int(input())
for _ in range(T):
    n = int(input())
    room = 0
    for i in range(1, n):
        if i ** 2 <= n:
            room += 1
        elif i ** 2 > n:
            break
    print(room)
# 주어진 n개의 방 중에서 제곱수의 개수를 구하지 않고
# 1부터 n - 1까지 모든 수에 대해 제곱을 구하여 비교함
# 시간복잡도가 O(n)으로 비효율적
# 큰 입력값에 대해서는 느리게 동작할 수 있음



# 2.
from math import floor

T = int(input())
for _ in range(T):
    n = int(input())
    print(floor(n ** 0.5))
# 주어진 n개의 방 중에서 제곱수의 개수를 하는 방법
# floor 함수를 사용해서 n의 제곱근을 구한 후 내림한 값으로 제곱근의 개수를 구함
# 시간복잡도가 O(1)로 매우 효율적
# 큰 입력값에 대해서도 빠르게 동작




# 각 단계에서 열려있는 방들을 선택하기 위해서는 숫자의 제곱근을 이용할 수 있다
# 우선 문제에서 주어진 규칙에 따라 방의 문 상태를 변경할 때
# 각 단계에서는 일정한 규칙에 따라 문의 상태가 변화한다
# 이때 방의 번호가 제곱수인 경우에는 해당 방의 문 상태가 바뀌게 된다.
# 예를 들어 1부터 10까지의 방이 있다고 가정할 때
# 1은 1의 제곱수, 4, 8은 2의 제곱수, 9는 3의 제곱수이므로 각 방의 문 상태가 바뀌게 된다
# 이를 제외한 나머지 번호는 제곱수가 아니므로 방의 문 상태가 바뀌지 않는다
# 따라서 n개의 방 중에서 제곱수의 개수를 알아내면
# 각 단계에서 열려 있는 방의 개수를 구할 수 있다