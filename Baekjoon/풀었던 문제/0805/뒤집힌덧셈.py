# 1357
# 어떤 수 X가 주어졌을 때 X의 모든 자리수가 역순이 된 수를 얻을 수 있다
# Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자
# 예 : X = 123 일 때 Rev(X) = 321
# 그리고 X = 100 일 때 Rev(X) = 1
# 두 양의 정수 X와 Y가 주어졌을 때
# Rev(Rev(X) + Rev(Y))를 구하는 프로그램 작성

# 출력 예시
# 223

import sys
sys.stdin = open('뒤집힌덧셈.txt')

X, Y = map(int, input().split())

revX = int(str(X)[::-1])
revY = int(str(Y)[::-1])

sum_ = revX + revY
revSum = int(str(sum_)[::-1])

print(revSum)