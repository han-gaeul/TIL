# 5613

# 덧셈, 뺄셈, 곱셈, 나눗셈을 할 수 있는 계산기 프로그램을 만드시오

# 입력의 각 줄에는 숫자와 +, -, *, /, = 중 하나가 교대로 주어진다
# 첫번째 줄은 수이다
# 연산자의 우선 순위는 생각하지 않으며 입력 순서대로 계산을 하고
# =가 주어지면 그때까지의 결과를 출력한다
# 나눗셈에서 소수점은 버린다

# 첫째 줄에 계산 결과를 출력

res = int(input())
while True:
    op = input()
    if op == '=':
        break
    n = int(input())
    if op == '+':
        res += n
    elif op == '-':
        res -= n
    elif op == '*':
        res *= n
    elif op == '/':
        res //= n
print(res)