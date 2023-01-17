# 알파벳 소문자로 이루어진 N개의 단어가 들어오면
# 아래와 같은 조건에 따라 정렬하는 프로그램 작성
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

# 첫째 줄에 단어의 개수 N이 주어진다
# 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가
# 한 줄에 하나씩 주어진다

# 조건에 따라 정렬하여 단어들을 출력
# 같은 단어가 여러 번 입력된 경우 한 번씩만 출력

import sys
input = sys.stdin.readline

n = int(input())
list_ = []

for i in range(n):
    list_.append(input().strip())

# 중복값 제거
set_list_ = set(list_)
list_ = list(list_)

# 알파벳 순서대로 정렬
list_.sort()
# 문자열 길이 순으로 정렬
list_.sort(key = len)

for i in list_:
    print(i)

# 변수명만 바꿨는데 틀림 이해가 안 됨

#! -------------------------------

import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
set_lst = set(lst)
lst = list(set_lst)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)