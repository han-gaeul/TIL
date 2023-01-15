# 정수가 들어있는 배열 num_list가 매개변수로 주어진다
# num_list의 원소의 순서를 거꾸로 뒤집은 배열 return

# reverse
def solution(num_list):
    num_list.reverse()
    return num_list

# 슬라이싱
def solution(num_list):
    return num_list[::-1]