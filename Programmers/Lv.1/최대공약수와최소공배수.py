# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환
# 예를 들어 3, 12의 최대공약수는 3, 최소공배수는 12이므로
# [3, 12]를 반환

import math

def solution(n, m):
    gcd_value = math.gcd(n, m)
    lcm_value = n * m // math.gcd(n, m)
    return [gcd_value, lcm_value]


# gcd의 경우 내장함수로 간편하게 계산이 가능하지만
# lcm 함수의 경우 python 3.9 버전 이상부터 사용이 가능하다고 한다
# 그래서인지 프로그래머스에서는 오답 처리...
# 어쩔 수 없이 gcd를 이용해 lcm 값을 계산하고
# 리스트에 담아 반환했다