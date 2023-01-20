# 이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어진다
# 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인
# 직사각형 형태를 출력


# 1.
a, b = map(int, input().split())

for i in range(b):
    print('*' * a)


# 2.
a, b = map(int, input().split())
print(('*' * a + '\n') * b)