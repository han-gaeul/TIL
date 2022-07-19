# 등차를 계속 더해 n번째 항을 구한다. (반복문 사용)
# 등차수열 공식 사용

from re import A


x, y, z = map(int, input().split())

# while문
i, result = 1, x

while i < z:
    result += y
    i += 1
print(result)


# for문
result = x

for i in range(z - 1):
    result += y
print(result)


# 등차수열 공식
print(x + y * (z - 1))

# 반복문 사용시 주의할 점
# 등차수열은 x, x + y, x + y + y로 증가
# -> while문에서 i = 1, for문에서 range(z - 1)인 이유
# 초기값이 x이므로 첫번째 반복문에서는 y가 더해지지 않음
# z가 아닌 z - 1번 반복해야 함