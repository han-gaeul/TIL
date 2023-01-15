# 정수가 담긴 리스트 num_list가 주어질 때
# num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return

def solution(num_list):
    even = 0
    odd = 0

    for x in num_list:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    return [even, odd]