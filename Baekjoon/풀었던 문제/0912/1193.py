# X가 주어졌을 때 X번째 분수를 구하는 프로그램 작성

# 첫째 줄에 X가 주어진다

# 첫째 줄에 분수를 출력

x = int(input())
line = 1

while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    a = x
    b = line - x + 1
else:
    a = line - x + 1
    b = x

print(a, '/', b, sep='')

# 입력 받은 x를 1씩 늘려가며 빼서 몇 번째 줄에 몇 번째 숫자인지 구하고
# 짝수번째 줄인지 홀수번째 줄인지에 따라 분바, 분모의 숫자의
# 방향이 홀수 줄인 경우 분자는 내림차순, 분모를 오름차순이고
# 짝수 줄인 경우 그 반대