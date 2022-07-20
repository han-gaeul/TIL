# 수 나열하기
# 시작값(a), 곱할 값(m), 더할 값(b), 몇 번째인지 나타내는 정수(n)가 입력 될 때
# n번째 수를 출력

a, m, d, n = map(int, input().split())

for i in range(1, n):
    a = a * m + d

print(a)