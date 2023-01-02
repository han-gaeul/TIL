# 정수 배열 array가 매개변수로 주어질 때
# 가장 큰 수와 그 수의 인덱스를 담은 배열을 return

def solution(array):
    answer = []
    max_num = max(array)
    answer.append(max_num)
    idx = array.index(max_num)
    answer.append(idx)
    return answer