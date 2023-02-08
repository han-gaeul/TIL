# 9506

# 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면
# 그 수를 완전수라고 한다
# 예를 들어 6은 6 = 1 + 2 + 3으로 완전수이다
# n이 완전수인지 아닌지 판단해보자

# 입력은 테스트 케이스마다 한 줄 간격으로 n이 주어진다
# 입력의 마지막엔 -1이 주어진다

# 테스트케이스마다 한줄에 하나씩 출력해야 한다
# n이 완전수라면 n을 n이 아닌 약수들의 합으로 나타내어 출력한다
# 이때 약수들은 오름차순으로 나열해야 한다
# n이 완전수가 아니라면 n is NOT perfect. 를 출력

while True:
    n = int(input())
    divisor = []
    if n == -1:
        break
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
    if sum(divisor) == n:
        print(n, " = ", " + ".join(str(i) for i in divisor), sep="")
    else:
        print(n, 'is NOT perfect.')