# 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 한다.
# 다항식을 계산할 때는 동류항끼리 계산해 정리한다.
# 덧셈으로 이루어진 다항식 polynomial이
# 매개변수로 주어질 때 동류항끼리 더한 결괏값을
# 문자열로 return. 같은 식이라면 가장 짧은 수식 return

def solution(polynomial):
    x, num = 0, 0
    # 수식을 연산자와 분리
    polynomial = polynomial.split(" + ")
    # 분리한 배열을 순회하면서
    for i in polynomial:
        # 해당 값에 x가 포함 되어 있늕 판별
        if 'x' not in i:
            # x가 포함 되어 있지 않다면 num 변수의 값을 증가
            num += int(i)
        else:
            # i의 길이가 1이라면 i == 'x' 라고 생각하고
            # x의 값에 1만 더함
            if len(i) == 1:
                x += 1
            else:
                # x의 길이가 1이 아니라면 x 앞에 있는 문자열을
                # 더해야 하기 때문에 슬라이싱을 하고
                # 해당 값을 x에 더함
                x += int(i[:-1])
    # 예외처리
    if x == 0 and num == 0:
        return
    if x == 0:
        return str(num)
    if x == 1:
        x = ""
    if num == 0:
        return str(x) + "x"
    return str(x) + "x + " + str(num)