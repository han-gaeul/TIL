# 음이 아닌 정수를 9로 나눈 나머지는 그 정수의 각 자리
# 숫자의 합을 9로 나눈 나머지와 같은 것이 알려져 있다
# 이 사실을 이용해 음이 아닌 정수가 문자열 number로
# 주어질 때, 이 정수를 9로 나눈 나머지를 return

def solution(number):
    num_sum = sum(int(i) for i in number)
    ans = num_sum % 9
    return ans