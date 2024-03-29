# 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는
# 정수 k들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 한다
# 단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용
# X, Y의 짝꿍이 존재하지 않으면 짝꿍은 -1이다
# X, Y의 짝꿍이 0으로만 구성되어 있다면 짝꿍은 0이다
# 예를 들어 X = 3404이고 Y = 13203이라면
# X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로
# 만들 수 있는 가장 큰 정수인 330이다
# 다른 예시로 X = 5525, Y = 1255이면 X와 Y의 짝꿍은
# X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는
# 가장 큰 정수인 552이다. X에는 5가 3개, Y에는 5가 2개 나타나므로
# 남는 5 한 개는 짝 지을 수 없다
# 두 정수 X, Y가 주어졌을 때 X, Y의 짝꿍을 return

def solution(X, Y):
    answer = ''
    # 숫자는 0 ~ 9만 반복되므로 9부터 0까지 반복
    # 짝꿍을 만들 때 큰 수부터 더하면 자동으로 제일 큰 수가 됨
    for i in range(9, -1, -1):
        # X, Y에 i가 몇 개인지 count 함수로 세고 그 중에서 작은 수를
        # 문자열로 변환한 i와 곱함
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
    # 짝꿍이 없을 경우
    if answer == '':
        return '-1'
    # 짝꿍이 0으로만 구성될 경우
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer