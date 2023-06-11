# 문자열 binomial이 매개변수로 주어진다
# binomial은 a op b 형태의 이항식이고 a와 b는 음이 아닌 정수,
# op는 +, -, * 중 하나이다. 주어진 식을 계산한 정수를 return

def solution(binomial):
    a, op, b = binomial.split()
    a, b = int(a), int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a* b