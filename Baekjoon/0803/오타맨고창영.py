# 백준 2711
# 창영이가 오타를 낸 문장과 오타를 낸 위치가 주어졌을 때
# 오타를 지운 문자열을 출력
# 창영이는 오타를 반드시 1개만 낸다.

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다
# 첫 숫자는 창영이가 오타를 낸 위치
# 두 번째 문자열은 창영이가 친 문자열
# 문자열의 가장 첫 문자는 1번째 문자이고 대문자로만 이루어져 있음
# 오타를 낸 위치는 문자열 길이보다 작거나 같다

# 오타를 지운 문자열 출력

import sys

sys.stdin = open('오타맨고창영.txt', 'r')

T = int(input())

for i in range(T):
    n, wrong_word = input().split()
    n = int(n)
    print(wrong_word[:n - 1], wrong_word[n:], sep = '')

# 예 : 4 MISSPELL -> MISPELL 이라면
# wrong_word[:3] = MIS
# wrong_word[4:] = PELL
# 즉 오타의 위치가 4인 경우 word[:3] + word [4:] 출력