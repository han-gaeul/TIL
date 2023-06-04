# 정수가 있을 때, 짝수라면 반으로 나누고, 홀수라면 1을 뺀 뒤
# 반으로 나누면, 마지막엔 1이 된다
# 예를 들어 10이 있다면 다음과 같은 과정으로 1이 된다
# 10 / 2 = 5
# (5 - 1) / 2 = 4
# 4 / 2 = 2
# 2 / 2 = 1
# 위와 같이 4번의 나누기 연산으로 1이 되었다
# 정수들이 담긴 리스트 num_list가 주어질 때, num_list의
# 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수를 return

def solution(num_list):
    cnt = 0
    for num in num_list:
        while num > 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = (num - 1) // 2
            cnt += 1
    return cnt