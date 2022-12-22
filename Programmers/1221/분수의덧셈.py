# 첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1
# 두 번째 분수의 분자와 분모를 뜻하는 denum2, num2
# 두 수가 매개변수로 주어진다
# 두 분수를 더한 값을 기약 분수로 나타냈을 때
# 분자와 분모를 순서대로 담은 배열을 return 하도록
# solution 함수 완성

# 두 개의 분수가 주어질때 그 분수의 합을 기약분수의 형태로 반환

# 1. 단순 gcd 활용
def solution(denum1, num1, denum2, num2):
    # 두 분수의 합 계산
    boonmo = num1 * num2
    boonja = denum1 * num2 + denum2 * num1

    # 최대 공약수 계산
    start = max(boonmo, boonja) # 두 숫자 중 더 큰 값을 가져감
    gcd_value = 1 # gcd의 결과를 담을 변수

    for num in range(start, 0, -1):
        # num이 boonmo와 boonja의 약수인지 확인
        if boonmo % num == 0 and boonja % num == 0:
            gcd_value = num # 두 가지 조건이 맞다면 gcd_value에 num을 담아줌
            break
    
    # gcd로 나눈 값을 answer에 담기
    answer = [boonja / gcd_value, boonmo / gcd_value]
    return answer


# 2. 최적화된 gcd를 활용
# 재귀함수 형태..
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def solution(denum1, num1, denum2, num2):
    # 두 분수의 합 계산
    boonmo = num1 * num2
    boonja = denum1 * num2 + denum2 * num1

    # 최대 공약수 계산
    gcd_value = gcd(boonmo, boonja)

    # gcd로 나눈 값을 answer에 담기
    answer = [boonja / gcd_value, boonmo / gcd_value]
    return answer


# 3. math 라이브러리를 활용
# 가장 효율적임
import math

def solution(denum1, num1, denum2, num2):
    # 두 분수의 합 계산
    boonmo = num1 * num2
    boonja = denum1 * num2 + denum2 * num1

    # 최대 공약수 계산
    gcd_value = math.gcd(boonmo, boonja)

    # gcd로 나눈 값을 answer에 담기
    answer = [boonja / gcd_value, boonmo / gcd_value]
    return answer