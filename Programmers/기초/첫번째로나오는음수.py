# 정수 리스트 num_list가 주어질 때 첫번째로 나오는
# 음수의 인덱스를 return
# 음수가 없다면 -1 return

def solution(num_list):
    for i, num in enumerate(num_list):
        if num < 0:
            return i
    return -1