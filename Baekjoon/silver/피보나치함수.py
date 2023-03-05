# 1003

# 다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다
# int fibonacci(int n) {
#     if (n == 0) {
#         printf("0");
#         return 0;
#     } else if (n == 1) {
#         printf("1");
#         return 1;
#     } else {
#         return fibonacci(n‐1) + fibonacci(n‐2);
#     }
# }
# fibonacci(3)을 호출하면 다음과 같은 일이 일어난다
# fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫번째 호출)을 호출한다
# fibonacci(2)는 fibonacci(1) (두번째 호출)과 fibonacci(0)을 호출한다
# 두번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다
# fibonacci(0)은 0을 출력하고 0을 리턴한다
# fibonacci(2)는 fibonacci(1)돠 fibonacci(0)의 결과를 얻고, 1을 리턴한다
# 첫번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다
# fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고 2를 리턴한다
# 1은 2번 출력되고 0은 1번 출력된다
# N이 주어졌을 때 fibonacci(N)을 호출했을 때
# 0과 1이 각각 몇번 출력되는지 구하라

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다
# 각 테스트 케이스는 한 줄로 이루어져 있고 N이 주어진다

# 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력

T = int(input())
# 0과 1이 나온 횟수를 저장할 리스트 초기화
zero = [1, 0, 1]
one = [0, 1, 1]
def fibonacci(num):
    length = len(zero)
    # num이 리스트 길이보다 크다면 리스트에 값 추가
    if num >= length:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print('{} {}'.format(zero[num], one[num]))
for _ in range(T):
    fibonacci(int(input()))


# zero 리스트와 one 리스트의 초기값은 각각 [1, 0, 1]과 [0, 1, 1]이다
# 피보나치 수열을 이용한 코드에서 초기값으로 사용되는
# [0, 1]과 [1, 0]을 민들기 위한 초기값이다.
# 피보나치 수열을 구하는 방법 중에는 이전 항과 그 이전 항의 합으로 이루어진
# 수열로 만드는 방법이 있는데 이 경우 초기값으로 [0, 1]이 들어가기 때문에
# 초기값이 [1, 0, 1]과 [0, 1, 1]이 된다

# length는 현재 0과 1이 저장된 리스트의 길이를 나타낸다
# 이 길이가 num보다 작은 경우 이미 저장된 값들을 활용해
# N번째 피보나치 수열의 0과 1이 출력된 횟수를 계산할 수 있다
# for 문을 통해 i가 length부터 num까지 반복하며
# zero와 one 리스트에 0과 1이 각각 몇번 출력됐는지를 계산하여 추가한다
# 이때 피보나치 수열의 점화식을 이용해 zero[i]와 one[i]를 계산한다
# zero[i]는 i번째 피보나치 수열에서 0이 몇 번 출력되는지 나타내고
# one[i]는 1이 몇 번 출력되는지 나타낸다
# zero[i]와 one[i]는 각각 zero[i - 1], one[i - 1]과
# zero[i - 2], one[i - 2]를 더한 값으로 계산된다
# 이는 피보나치 수열에서 각 항이 그 이전 항 두 개를 더한 값이기 때문이다
# 따라서 zero[i]와 one[i]를 계산하여 리스트에 추가하는 것으로
# N번째 피보나치 수열에서 0과 1이 각각 몇 번 출력되는지 구할 수 있다