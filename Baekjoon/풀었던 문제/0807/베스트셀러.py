# 1302
# 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때
# 가장 많이 팔린 책의 제목을 출력

# 첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다
# 둘째부터 N개의 줄에 책의 제목이 입력으로 주어진다
# 책의 제목은 알파벳 소문자로만 이루어져 있다

# 만약 가장 많이 팔린 책이 여러 개일 경우 사전 순으로 가장 앞서는 제목 출력

import sys
sys.stdin = open('베스트셀러.txt')

N = int(input())
bookDic = {}

for i in range(N):
    book = input()
    #* 딕셔너리에 책이 저장되어 있지 않다면
    if book not in bookDic:
        bookDic[book] = 1
    #* 저장되어 있다면 +1을 해서 책의 개수를 셈
    else:
        bookDic[book] += 1

#* 가장 많이 팔린 책의 제목을 저장할 수 있는 리스트
list = []
#* 가장 많이 팔린 책의 개수를 num에 저장
num = max(bookDic.values())

#* 딕셔너리를 순회하면서
for i in bookDic:
    #* num에 해당되는 값을 가진 요소가 있다면
    if num == bookDic[i]:
        #* 리스트에 책 제목 추가
        list.append(i)

#* 리스트를 사전 순으로 정렬하고
list.sort()
#* 리스트의 제일 앞의 값만 출력
print(list[0])