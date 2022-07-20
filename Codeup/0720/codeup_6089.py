# 수 나열하기
# 시작값(a), 등비(r), 몇 번째인지 나타내는 정수(n)가 입력 될 때
# n번째 수를 출력

a, r, n = map(int, input().split())

print(a * r ** (n - 1))