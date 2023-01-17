# X보다 작은 수
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다
# 이때, A에서 X보다 작은 수를 모두 출력

# 첫째 줄에 N과 X가 주어진다
# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다.
# X보다 작은 수를 입력 받은 순서대로 공백으로 구분해 출력
# X보다 작은 수는 적어도 하나 존재

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in A:
    if X > i:
        print(i, end = ' ')
    else:
        continue