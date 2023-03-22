# 두 수의 최소공배수란 입력된 두 수의 배수 중 공통이 되는
# 가장 작은 숫자를 의미한다. 예를 들어 2와 7의 최소공배수는
# 14가 된다. 정의를 확장해서, n개의 수의 최소공배수는 n개의
# 수들의 배수 중 공통이 되는 가장 작은 숫자가 된다.
# n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의
# 최소공배수를 return

from math import gcd

def solution(arr):
    answer = arr[0]
    for i in arr:
        answer = answer * i // gcd(answer, i)
    return answer



# 반복문에서는 각 숫자 i에 대해서 현재까지의 최소공배수
# answer와 i의 GCD를 구한 뒤, answer에 i를 곱하고
# GCD로 나눈 값을 저장한다.

# 최소공배수(LCM)는 두 수의 곱을 최대공약수(GCD)로
# 나눈 것과 같다. 이를 확장하면 n개의 수들의 LCM은
# n개의 수의 곱을 모든 수의 GCD로 나눈 것과 같아진다
# 따라서 주어진 배열 arr의 LCM을 구하기 위해선,
# arr의 모든 수들을 곱한 후에 모든 수들의 GCD로 나누어준다.
# 그러나 모든 수의 GCD를 구하려면 시간복자도가 매우
# 커지기 때문에 위의 코드에서는 유클리드 알고리즘을
# 이용한 math.gcd()를 이용해서 각 수마다 GCD를 계산하고
# answer과 곱해 새로운 answer를 만들어가는 방식으로
# LCM을 구한다.