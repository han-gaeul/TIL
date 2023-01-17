# 블랙잭의 규칙은 카드의 합이 21을 넘지 않는 한도 내에서
# 카드의 합을 최대한 크게 만드는 게임
# 한국 최고의 블랙잭 고수 버전의 블랙잭에서 각 카드에는
# 양의 정수가 적혀있다. 그 다음 딜러는 N장의 카드를 모두
# 숫자가 보이도록 바닥에 놓는다. 그 후에 딜러는 숫자 M을 크게 외친다
# 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 고른다
# 블랙잭 변형 게임이기 때문에 플레이어가 고른 카드의 합은
# M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다
# N장의 카드에 쓰여 있는 숫자가 주어졌을 때
# M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력

# 첫째 줄에 카드의 개수 N과 M이 주어진다
# 둘째 줄에는 카드에 쓰여 있는 수가 주어진다
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다

# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력


n, m = map(int, input().split())
cardNumber = list(map(int, input().split()))
result = 0

# 3개의 카드를 뽑아야 하며 이에 대한 모든 경우의 수를
# 살펴보기 위해 3중 for문을 사용
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # 세 카드의 합이 m보다 크면 continue
            if cardNumber[i] + cardNumber[j] + cardNumber[k] > m:
                continue
            # m보다 크지 않으면 result에 저장
            # 이렇게 하면 result에는 m의 값 또는 m에 가장 가까운 값이 저장 됨
            else:
                result = max(result, cardNumber[i] + cardNumber[j] + cardNumber[k])

print(result)