# 4504

# 정수 n과 수의 목록이 주어졌을 때 목록에 들어있는 수가
# n의 배수인지 아닌지 구하라

# 첫째 줄에 n이 주어진다
# 다음 줄부터 한 줄에 한 개씩 목록에 들어있는 수가 주어진다
# 목록은 0으로 끝난다

# 목록에 있는 수가 n의 배수인지 아닌지 구한뒤 예제처럼 출력

# 1 is NOT a multiple of 3.
# 7 is NOT a multiple of 3.
# 99 is a multiple of 3.
# 321 is a multiple of 3.
# 777 is a multiple of 3.


# 1.
n = int(input())
while True:
    num = int(input())
    if n == 0:
        break
    if num % n == 0:
        print('{} is a multiple of {}.'.format(num, n))
    else:
        print('{} is NOT a multiple of {}.'.format(num, n))
# 런타임에러(EOFError)
# 입력이 더이상 없는 경우에도 코드가 종료되지 않고 무한히 대기하기 때문에 에러 발생
# try-except문으로 에러를 처리할 수 있지만 백준에서는 정답처리 되지 않음


# 2.
n = int(input())
while 1:
    a = int(input())
    if a == 0 :
        break
    if a % n == 0 :
        print("{} is a multiple of {}.".format(a, n))
    else :
        print("{} is NOT a multiple of {}.".format(a, n))
# 입력받은 문자열이 '0'인지 검사하여 종료하는 방식
# 입력이 없을 때는 자연스럽게 종료된다.