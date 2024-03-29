# 2748

# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고 1번째 피보나치 수는 1이다
# 그다음 2번째부터는 바로 앞 피보나치 수의 합이 된다
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2가 된다
# n = 17일때까지 피보나치 수를 써보면 다음과 같다
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
# n이 주어졌을 때 n번째 피보나치 수를 구하라

# 첫째 줄에 n이 주어진다

# 첫째 줄에 n번째 피보나치 수를 출력

n = int(input())
fibonacci = [0, 1]
for i in range(2, n + 1):
    num = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(num)
print(fibonacci[n])