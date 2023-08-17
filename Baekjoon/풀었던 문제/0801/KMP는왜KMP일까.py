# 백준 2902
# KMP 인 이유는 이를 만든 사람의 성이
# Knuth, Morris, Prett이기 때문

# 이렇게 사람 성이 들어간 알고리즘을 두 가지 형태로 부른다
# 첫 번째는 성을 모두 쓰고 이를 하이픈으로 이어 붙인 것
# 예를 들면 Knuth-Morris-Pratt. 이것을 긴 형태.
# 두 번째로 짧은 형태는 만든 사람의 성의 첫 글자만 따서 부른 것.
# 예를 들면 KMP

# 긴 형태의 알고리즘이 주어졌을 때
# 이를 짧은 형태로 바꾸어 출력

# 입력은 한 줄로
# 첫 번째 글자는 항상 대문자
# 그리고 하이픈 뒤에는 반드시 대문자
# 그 외의 모든 문자는 소문자


import sys

# input = sys.stdin.readline
sys.stdin = open('KMP는왜KMP일까?.txt', 'r')

a = list(input().split('-'))

for i in a:
    print(i[0], end = '')

# -를 기준으로 list형으로 입력 받음
# 입력 받은 문자열의 첫번째만 출력
# end = '' 를 추가하면 줄바꿈, 띄어쓰기 없이 출력
