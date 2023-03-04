# 6588

# 1742년 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트
# 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다
# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다
# 예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다
# 또 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 + 19 + 23이다
# 이 추측은 아직도 해결되지 않은 문제이다
# 백만 이하의 모든 짝수에 대해서 이 추측을 검증하라

# 입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다
# 각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다
# 입력의 마지막 줄에는 0이 하나 주어진다

# 각 테스트 케이스에 대해서 n = a + b 형태로 출력한다
# 이때 a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다
# 만약 n을 만들 수 있는 방법이 여러가지라면 b - a가 가장 큰 것을 출력
# 또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 
# 'Goldbach's conjecture is wrong.'을 출력


# 1.
import sys

# 자연수를 소수인지 아닌지 저장하는 배열
arr = [True for i in range(1000001)]
# 에라토스테네스의 체 알고리즘 이용해 소수 구하기
for i in range(2, 1001):
    if arr[i]:
        for j in range(i + i, 1000001, i):
            arr[j] = False
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(3, len(arr)):
        if arr[i] and arr[n - i]:
            print(n, '=', i, '+', n - i)
            break
# pypy3 784ms
# 2부터 1000000까지 소수를 구한 후 입력으로 주어진 n을
# 만들 수 있는 소수를 찾는다



# 2.
import sys

arr = [False, False] + [True] * 1000000
for i in range(2, 1001):
    if arr[i] == True:
        for j in range(i + i, 1000001, i):
            arr[j] = False
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    A = 0
    B = n
    for _ in range(1000000):
        if arr[A] and arr[B]:
            print(f"{n} = {A} + {B}")
            break
        A += 1
        B -= 1
    else:
        print("Goldbach's conjecture is wrong.")
# pypy3 504ms
# 입력으로 주어진 n을 만들 수 있는 두 소수를 찾을 때
# 첫번째 소수를 0부터 1000000까지 하나씩 증가시키고
# 두번째 소수를 n부터 0까지 하나씩 감소시킨다