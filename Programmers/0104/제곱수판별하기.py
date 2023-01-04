# 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 한다
# 정수 n이 매개변수로 주어질 때 n이 제곱수라면 1,
# 아니라면 2를 return


def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2


# is_integer()
# float 객체가 정수라면 True
# 그렇지 않으면 False 반환
# 예를 들어 1.5.is_integer()는 False
# 1.0.is_integet()는 True