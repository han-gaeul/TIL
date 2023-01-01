# 군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를
# 사용하는 것을 알아냈다.
# 1. 암호화된 문자열 cipher를 주고 받는다
# 2. 그 문자열에서 code의 배수 번째 글자만 진짜 암호이다
# 문자열 cipher와 정수 code가 매개변수로 주어질 때
# 해독된 암호 문자열을 return

def solution(cipher, code):
    answer = cipher[code -1::code]
    return answer