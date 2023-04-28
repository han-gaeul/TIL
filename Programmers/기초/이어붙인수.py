# 정수가 담긴 리스트 num_list가 주어진다
# num_list의 홀수만 순서대로 이어 붙인 수와 짝수만
# 순서대로 이어 붙인 수의 합을 반환

def solution(num_list):
    odd = ''.join([str(i) for i in num_list if i % 2 == 1])
    even = ''.join([str(i) for i in num_list if i % 2 == 0])
    return int(odd) + int(even)