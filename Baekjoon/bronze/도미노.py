# 2921

# 도미노는 여러 종류의 타일 게임에서 사용하는 조각이다
# 도미노 조각은 두 칸으로 이루어져 있다. 각 칸에는 점이 찍혀있는데
# 점이 안 찍혀져 있을 수도 있다. 점의 개수는 세트의 크기에 의해서 결정된다.
# 세트의 크기가 N인 도미노 세트에서 점의 개수는 0보다 크거나 같고 N보다 작거나 같다
# 두 도미노에 찍혀있는 점의 개수가 같다면 두 도미노는 동일한 것이다
# 예를 들어 점이 2개와 8개 찍혀있는 도미노는 8개와 2개 찍혀있는 도미노와 같은 도미노이다
# 크기가 N인 도미노 세트는 N 또는 그보다 작거나 같은 점을 포함하는 가능한 도미노를
# 모두 포함하고 있고 각 도미노는 중복되지 않는다.
# N을 입력받은 뒤 크기가 N인 도미노 세트에는 점이 몇 개 찍여있는지 구하라

# 첫째 줄에 도미노 세트의 크기 N이 주어진다

# 크기가 N인 도미노 세트에 찍혀있는 점의 개수 출력



# 1.
from itertools import combinations_with_replacement

N = int(input())
result = 0
for i in combinations_with_replacement(range(N + 1), 2):
    result += sum(i)
print(result)

# combinations_with_replacement(iterable, x)
# iterable에서 원소 개수가 x개인 중복 조합 뽑기


# 2.
N = int(input())
result = 0
for i in range(N + 1):
    for j in range(i, N + 1):
        result += i + j
print(result)

# 시간효율이 더 좋음