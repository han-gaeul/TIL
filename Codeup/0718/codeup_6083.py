r, g, b = map(int, input().split())

for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(i, j, k)

print(r * g* b)

# 정수형으로 입력받은 뒤 for 반복문을 3중으로 사용하여
# 0, 0, 0부터 r-1, g-1, b-1 까지 모든 경우의 수 출력