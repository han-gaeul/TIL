# 문자열 my_string이 매개변수로 주어질 때
# 대문자는 소문자로, 소문자는 대문자로 변환한 문자열을 return

def solution(my_string):
    answer = ''
    for i in my_string:
        # i가 대문자인지 확인
        # 대문자라면
        if i.isupper():
            # 소문자로 변환하고 answer에 추가
            answer += i.lower()
        else:
            # 그렇지 않으면 대문자로 변환하고 answer에 추가
            answer += i.upper()
    return answer


# isupper()
# 문자열이 대문자면 True, 그렇지 않으면 False 반환
# islower()
# 문자열이 소문자면 True, 그렇지 않으면 False 반환