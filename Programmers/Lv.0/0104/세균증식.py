# 어떤 세균은 1시간에 두 배만큼 증식한다
# 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때
# t시간 후 세균의 수를 return

def solution(n, t):
    virus = n
    for i in range(t):
        virus *= 2
    return virus


def solution(n, t):
    return n * (2 ** t)


def solution(n, t):
    return n << t

# a << b 비트연산자
# 2를 곱한 것과 같음
# n << m : n * 2의 m승
# 예를 들어 2 << 2 같은 경우
# 0 : 2
# 1 : 2 * 2 = 4
# 2 : 4 * 2 = 8


# a >> b 비트연산자
# 2를 나눈 것과 같음
# n >> m : n / 2의 m승