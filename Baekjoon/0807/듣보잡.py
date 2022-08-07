# 1764
# 듣도 못한 사람의 명단과 보도 못한 사람의 명단이 주어질 때
# 듣도 보도 못한 사람의 명단을 구하는 프로그램

# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과
# N + 2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다
# 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며
# 명단에는 중복되는 이름이 없다.

# 수와 명단을 사전순으로 출력

import sys
sys.stdin = open('듣보잡.txt')

N, M = map(int, input().split())
#* 각각 중복이 없는 set의 특성을 활용해 
notHear = set()
notSee = set()

for _ in range(N):
    #* 입력 받은 문자들을 add
    notHear.add(input())

for _ in range(M):
    notSee.add(input())

#* set notHear, notSee의 교집합 &을 해서 중복되는 문자열을 선택하고
#* 리스트로 묶어 리스트화 한 후에 명단을 사전 순으로 제출하기 위해
#* sorted로 순서 정렬
result = sorted(list(notHear & notSee))

#* 수를 알기 위해 len 사용
print(len(result))

#* reuslt에 있는 값을 하나씩 출력
for i in result:
    print(i)