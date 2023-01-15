# my_string은 "3 + 5"처럼 문자열로 된 수식이다
# 문자열 my_string이 매개변수로 주어질 때
# 수식을 계산한 값을 return

def solution(my_string):
    return eval(my_string)

solution = eval


# eval()
# 수학 수식이 문자열 형식으로 들어오면
# 해당 수식을 계산한 결과를 반환