# 첫째 줄에 현재 시각이 나온다
# 현재 시각은 시 A와 분 B가 정수로 빈칸을 사이에 두고 순서대로 주어진다
# 두 번째 줄에는 요리하는데 필요한 시간 C가 분 단위로 주어진다

# 첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력

A, B = map(int, input().split())
C = int(input())

# 시와 분으로 나눠 각각 더함
A += C // 60
B += C % 60

# 더한 값으로 B값이 60 이상이면
# A에 1을 더하고 B에 60을 뺌
if B >= 60:
    A += 1
    B -= 60

# 0시 0분이 되는 부분을 처리하기 위해
# A가 24와 같거나 커지면 24를 뺌
if A >= 24:
    A -= 24

print('%d %d' % (A, B))