# String형 배열 seoul의 element 중 "Kim"의 위치 x를 찾아
# "김서방은 x에 있다"는 String을 return
# seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 있는 경우는 없다

def solution(seoul):
    answer = "김서방은 {}에 있다".format(seoul.index("Kim"))
    return answer