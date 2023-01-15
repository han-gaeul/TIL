# 문자열 my_string이 매개변수로 주어진다
# my_string은 소문자, 대문자, 자연수로만 구성된다.
# my_string 안의 자연수들의 합을 return

import re

def solution(my_string):
    # findall()을 이용해 숫자만 불러온다
    # 이때 +를 사용해 숫자가 2개 이상 붙어있으면 같이 불러온다
    answer = re.findall(r'[0-9]+', my_string)
    result = 0
    for i in answer:
        result += int(i)
    return result