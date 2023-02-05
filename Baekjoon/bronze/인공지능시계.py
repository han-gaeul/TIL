# 2530

# KOI 전자에서는 건강에 좋고 맛있는 훈제오리구이 요리를
# 간편하게 만드는 인공지능 오븐을 개발하려고 한다
# 인공지능 오븐을 사용하는 방법은 적당한 양의 오리 훈제 재료를
# 인공지능 오븐에 넣으면 된다. 그러면 인공지능 오븐은 오븐구이가
# 끝나는 시간을 초 단위로 자동적으로 계산한다
# 또한 KOI 전자의 인공지능 오븐 앞면에는 사용자에게 훈제오리구이
# 요리가 끝나는 시각을 알려주는 디지털 시계가 있다
# 훈제오리구이를 시작하는 시각과 오븐구이를 하는데 필요한 시간이
# 초 단위로 주어졌을 때 오븐구이가 끝나는 시각을 계산하라

# 첫째 줄에 현재 시각이 나온다
# 현재 시각은 시 A, 분 B와 초 C가 정수로 빈 칸을 사이에 두고
# 순서대로 주어진다
# 두 번째 줄에는 요리하는데 필요한 시간 D가 초 단위로 주어진다

# 첫째 줄에 종료되는 시각의 시, 분, 초를 공백을 사이에 두고 출력

import sys

h, m, s = map(int, sys.stdin.readline().split())
time = int(sys.stdin.readline())
# 총 초의 수 계산
s += time
# s가 60보다 크면 m에 1을 더함
m += s // 60
# 위와 동일
h += m // 60
# 24시간을 기준으로 계산하고 결과 출력
print(h % 24, m % 60, s % 60)