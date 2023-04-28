# 정수가 담긴 리스트 num_list가 주어질 때
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을,
# 크면 0을 반환

def solution(num_list):
    product = 1
    sum_elements = 0
    for num in num_list:
        product *= num
        sum_elements += num
    if product < sum_elements ** 2:
        return 1
    else:
        return 0