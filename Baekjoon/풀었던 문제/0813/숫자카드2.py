# 10816
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다
# 숫자 카드를 N개 가지고 있으며 정수 M개가 주어졌을 때
# 이 수가 적혀있는 숫자 카드를 몇 개 가지고 있는지 구하라

# 첫째 줄에 가지고 있는 숫자 카드의 개수 N이 주어진다
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다
# 셋째 줄에는 M이 주어진다
# 넷째 줄에는 몇개 가지고 있는 숫자 카드인지 구해야 할
# M개의 정수가 주어지며 이 수는 공백으로 구분되어져 있다.

# 첫째 줄에 입력으로 주어진 M개의 수에 대해서
# 각 수가 적힌 숫자 카드를 몇 개 가지고 있는지 공백으로 구분해 출력

import sys
sys.stdin = open('숫자카드2.txt')

N = int(input())
cards = [*map(int, input().split())]
M = int(input())
candidate = [*map(int, input().split())]

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in candidate:
    result = count.get(target)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")