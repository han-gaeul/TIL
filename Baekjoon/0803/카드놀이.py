# 백준 2511
# 입력은 두 개의 줄로 이루어짐
# 첫 번째 줄에는 A가 늘어놓은 카드의 숫자들이 빈칸을 두고 순서대로 주어짐
# 두 번째 줄에는 B가 늘어놓은 카드의 숫자들이 빈칸을 두고 순서대로 주어짐

# 첫 번째 줄에는 게임이 끝난 후
# A와 B가 받은 총 승점을 순서대로 빈칸을 두고 출력
# 두 번째 줄에는 이긴 사람이 A인지 B인지 출력
# 만약 비기는 경우에는 문자 D를 출력

import sys
sys.stdin = open('카드놀이.txt', 'r')

A = list(map(int, input().split()))
B = list(map(int, input().split()))

AScore = 0 #* A 점수
BScore = 0 #* B 점수

history = 'D' #* 승패 기록

for i in range(10):
    #* 비길 경우
    if A[i] == B[i]:
        AScore += 1
        BScore += 1
    #* A가 이길 경우
    elif A[i] > B[i]:
        AScore += 3
        history = 'A'
    #* B가 이길 경우
    elif A[i] < B[i]:
        BScore += 3
        history = 'B'

#* A 스코어가 더 높을 경우 
if AScore > BScore:
    print(AScore, BScore)
    print('A')
#* B 스코어가 더 높을 경우
elif AScore < BScore:
    print(AScore, BScore)
    print('B')
#* A, B 스코어가 같을 경우
elif AScore == BScore:
    if history == 'A':
        print(AScore, BScore)
        print('A')
    elif history == 'B':
        print(AScore, BScore)
        print('B')
    elif history == 'D':
        print(AScore, BScore)
        print('D')
