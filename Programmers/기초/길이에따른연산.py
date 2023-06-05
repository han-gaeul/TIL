# 정수가 담긴 리스트 num_list가 주어질 때, 리스트의 길이가
# 11 이상이면 리스트에 있는 모든 원소의 합을,
# 10 이하이면 모든 원소의 곱을 return

def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    elif len(num_list) <= 10:
        res = 1
        for i in num_list:
            res *= i
        return res