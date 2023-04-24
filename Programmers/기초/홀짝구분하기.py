# 자연수 n이 주어졌을 때 만약 n이 짝수이면 n is even을
# 홀수이면 n is odd를 출력

n = int(input())
if n % 2 == 0:
    print(n, 'is even')
else:
    print(n, 'is odd')