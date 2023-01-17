# 백준 2920
# 다장조는 c d e f g a b C 총 8개 음으로 이루어짐
# 8개 음은 다음과 같이 숫자로 바꾸어 표현
# c는 1로, d는 2로, ..., C를 8로 바꿈

# 1부터 8까지 차례대로 연주한다면 ascending
# 8부터 1까지 차례대로 연주한다면 descending
# 둘 다 아니라면 mixed

# 첫째 줄에 8개의 숫자가 주어진다
# 숫자는 문제에서 설명한 음이며 1부터 8까지 숫자가 한 번씩 등장
# 첫째 줄에 ascending, descending, mixed 중 하나 출력

import sys
sys.stdin = open('음계.txt', 'r')

num = list(map(int, input().split()))

if num == sorted(num):
    print('ascending')
elif num == sorted(num, reverse=True):
    print('descending')
else:
    print('mixed')