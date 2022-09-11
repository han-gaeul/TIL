# 숫자 카드는 정수가 하나 적혀져 있는 카드
# 상근이는 숫자 카드 N개를 가지고 있다
# 정수 M개가 주어졌을 때 이 수가 적혀있는 숫자 카드를
# 가지고 있는지 아닌지 구하는 프로그램 작성

# 첫째 줄에 가지고 있는 숫자 카드의 개수 N이 주어진다
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다
# 두 숫자 카드에 같은 수가 적혀있는 경우는 없다
# 셋째 줄에는 M이 주어진다
# 넷째 줄에는 가지고 있는 숫자 카드인지 아닌지를
# 구해야 할 M개의 정수가 주어지며 이 수는 공백으로 구분되어져 있다

# 첫째 줄에 입력으로 주어진 M개의 수에 대해서
# 각 수가 적힌 숫자 카드를 가지고 있으면 1을
# 아니면 0을 공백으로 구분해 출력한다

import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

dic_ = {}
# 가지고 있는 카드를 모두 딕셔너리에 0(아무 숫자 가능)로 등록
for i in range(len(card)):
    dic_[card[i]] = 0

# 체크할 배열 check가 딕셔너리에 있으면 1, 없으면 0 출력
for j in range(m):
    if check[j] not in dic_:
        print(0, end = ' ')
    else:
        print(1, end = ' ')