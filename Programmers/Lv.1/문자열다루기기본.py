# 문자열 s의 길이가 4 혹은 6이고 숫자로만 구성 되어있는지 확인
# 예를 들어 s가 "a234"이면 False, "1234"라면 True

def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit() == True:
            return True
        else:
            return False
    else:
        return False


def solution(s):
    return len(s) in (4, 6) and s.isdigit()


# 컴프리헨션과 in 키워드를 사용해 문자열 s의 길이가
# 4 또는 6인지 확인하고 조건이 참이면 문자열이
# 숫자로만 구성 되어있는지(유효한 숫자인지) 확인한다.
# 전체 함수는 두 조건이 모두 참일 경우 True
# 그렇지 않으면 False를 반환한다.