# 정수 리스트 num_list가 주어진다
# 가장 첫번째 원소를 1번 원소라고 할 때 홀수번째 원소들의 합과
# 짝수번째 원소들의 합 중 큰 값을 return

def solution(num_list):
    odd_num = 0
    enve_num = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            enve_num += num_list[i]
        else:
            odd_num += num_list[i]
    return max(odd_num, enve_num)