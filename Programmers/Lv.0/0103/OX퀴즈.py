# 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는
# 문자열 배열 quiz가 매개변수로 주어진다
# 수식이 옳다면 'O', 틀리다면 'X'를 순서대로 담은 배열을 return

def solution(quiz):
    answer = []
    for q in quiz:
        # 주어진 수식을 공백으로 분리하여
        # 각각 x, operator, y, _, z 로 할당
        # _는 '=' 문자를 할당한 변수. 사용하지 않음
        x, operator, y, _, z = q.split()
        x, y, z = int(x), int(y), int(z)
        if operator == '+':
            answer.append('O' if x + y == z else 'X')
        elif operator == '-':
            answer.append('O' if x - y == z else 'X')
    return answer