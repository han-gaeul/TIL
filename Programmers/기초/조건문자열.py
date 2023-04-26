# 문자열에 따라 다음과 같이 두 수의 크기를 비교
# 두 수가 n과 m이라면 '>', '=' : n >= m
# '<', '=' : n <= m, '>', '!' : n > m, '<', '!' : n < m
# 두 문자열 ineq와 eq가 주어진다. ineq는 <와 > 중 하나고
# eq는 =와 ! 중 하나이다. 그리고 두 정수 n과 m이 주어질 때
# n과 m이 ineq와 eq의 조건에 맞으면 1을, 아니면 0을 반환

def solution(ineq, eq, n, m):
    if ineq == "<":
        if eq == "=":
            return int(n <= m)
        else:
            return int(n < m)
    else:
        if eq == "=":
            return int(n >= m)
        else:
            return int(n > m)