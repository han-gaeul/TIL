# 첫째 줄과 둘째 줄에 세 자리 자연수가 주어진다

# 첫째 줄부터 넷째 줄까지 차례대로 들어갈 값 출력

# 2360
# 3776
# 1416
# 181720

num1 = int(input())
num2 = int(input())

print(num1 * (num2 % 10))
print(num1 * ((num2 % 100) // 10))
print(num1 * (num2 // 100))
print(num1 * num2)

# ---------------------------------------

num1 = int(input())
num2 = input()

for i in range(len(num2), 0, -1):
    print(num1 * int(num2[i - 1]))

print(num1 * int(num2))
