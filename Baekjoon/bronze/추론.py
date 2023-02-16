# 1731

# 등차가 정수인 등차수열(어떤 수에 차례대로 일정한 수를 더해서 이루어지는 수열)은 2개의 숫자로 나타낼 수 있다
# P는 수열의 첫 번째 수이고, Q는 그 다음수가 되기 위해 바로 전의 수에 더해야 하는 수이다
# 예를 들어 P = 1, Q = 2이면 그 등차수열은 1, 3, 5, 7, ... 이 된다
# 등비가 정수인 등비수열(어떤 수에서 시작해 차례로 같은 수를 곱하여 만든 수열)은 등차수열과 비슷하게
# 2개의 숫자로 나타낼 수 있다. P는 수열의 첫 번째 수이고, Q는 그 다음수가 되기 위해 바로 전의 수에 곱해야 하는 수이다
# 예를 들어 P = 3, Q = 2이면 그 등비수열은 3, 6, 12, ... 이 된다
# 테디는 세상에서 수학을 제일 좋아해서 매일같이 이 수열이 등차수열인지 등비수열인지 정한 다음에 다음 수를 구한다
# 어떤 수열이 주어졌을 때 그 수열의 규칙이 등차수열인지 등비수열인지 결정한 후 다음에 등장할 수를 구하라

# 첫째 줄에 수열의 길이 N이 주어진다
# 둘째 줄부터 N개의 줄에 수열의 각 원소가 차례대로 주어진다
# 주어지는 수열은 등차수열이나 등비수열 중에 하나다

# 첫째 줄에 수열의 다음 원소를 출력

N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))
if li[1] - li[0] == li[2] - li[1]:
    arithmetic = li[2] - li[1]
    print(li[-1] + arithmetic)
elif li[2] / li[1] == li[1] / li[0]:
    geometric = int(li[1] / li[0])
    print(li[-1] * geometric)