# 백준 마라톤 대회가 열린다
# 42.195km를 달리는 이 마라톤은 모두가 참가하고 싶어했던 만큼
# 매년 모두가 완주해왔다. 단 한 명만 빼고
# 모두가 참가하고 싶어 안달인데 이런 백준 마라톤 대회에
# 참가해놓고 완주하지 못한 배부른 참가자 한 명은 누구일까?

# 첫째 줄에 참가자 수 N이 주어진다
# N개의 줄에는 참가자의 이름이 주어진다
# 추가적으로 주어지는 N - 1개의 줄에는 완주한 참가자의 이름이 쓰여있다
# 참가자들의 이름은 길이가 1보다 크거나 같고
# 20보다 작거나 같은 문자열이고 알파벳 소문자로만 이루어져 있다

# 마라톤을 완주하지 못한 참가자의 이름 출력

import sys
input = sys.stdin.readline

n = int(input())
people = {}

for _ in range(n):
    name = input().rstrip()

    if name in people:
        people[name] += 1
    else:
        people[name] = 1

for _ in range(n - 1):
    name = input().rstrip()
    people[name] -= 1

for p in people:
    if people[p]:
        print(p)
        break

# for문으로 n번 돌면서 참가자의 이름을 딕셔너리에 저장
# 동명이인이 있을 수 있음을 생각
# for문으로 n - 1번 돌면서 완주한 사람의 value에 -1
# value가 1인 사람이 완주하지 못한 참가자