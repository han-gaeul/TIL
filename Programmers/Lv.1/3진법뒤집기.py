# 자연수 n이 매개변수로 주어진다
# n을 3진법 상에서 앞뒤로 뒤집은 후 이를 다시 10진법으로 표현한 수를 return

def solution(n):
    answer = ''
    while n > 0:
        # n을 3으로 나눈 몫과 나머지 계산
        n, result = divmod(n, 3)
        # 나머지만 answer에 더함
        answer += str(result)
    return int(answer, 3)


# while문을 반복하다보면 앞뒤로 뒤집은 3진법으로 변환된 값을 얻을 수 있다
# int(x, n) : n진법으로 구성된 str형식의 수를 10진법으로 변환한다
# divmod() : 두 개의 숫자를 인자로 받아 몫과 나머지를 튜플 형태로 반환한다