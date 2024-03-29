# 더하기 사이클
# 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고
# 각 자리의 숫자를 더한다
# 그 다음 주어진 수의 가장 오른쪽 자리 수와
# 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다

# 예 : 26부터 시작. 2 + 6 = 8. 새로운 수는 68
# 6 + 8 = 14. 새로운 수는 84
# 8 + 4 = 12. 새로운 수는 42
# 4 + 2 = 6. 새로운 수는 26
# 위의 예는 4번만에 원래 수로 돌아온다. 따라서 26의 사이클 길이는 4
# N이 주어졌을 떄 N의 사이클의 길이 출력

N = int(input())
num = N

# 사이클 수
count = 0

while True:
    a = num // 10 # 68의 정수 부분의 몫인 6
    b = num % 10 # 68의 나머지 부분인 8
    c = (a + b) % 10 # 6 + 8 = 14 중 나머지 부분인 4
    num = (b * 10) + c # 80 + 4 = 84

    count += 1
    if (num == N):
        break
print(count)