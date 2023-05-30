# 정수 리스트 num_list와 정수 n이 주어질 때
# num_list를 n번째 원소 이후의 원소들과 n번째까지의 원소들로
# 나눠 n번째 원소 이후의 원소들을 n번째까지의 원소들 앞에
# 붙인 리스트를 return

def solution(num_list, n):
    after_list = num_list[n:]
    before_list = num_list[:n]
    return after_list + before_list