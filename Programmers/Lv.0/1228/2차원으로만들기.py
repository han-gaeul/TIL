# 정수 배열 num_list와 정수 n이 매개변수로 주어진다
# num_list를 다음 설명과 같이 2차원 배열로 바꿔 return
# num_list가 [1, 2, 3, 4, 5, 6, 7, 8]로 길이가 8이고
# n이 2이므로 num_list를 2 * 4 배열로 다음과 같이 변경
# [[1, 2], [3, 4], [5, 6], [7, 8]]
# 2차원으로 바꿀 때는 num_list의 원소들을 앞에서부터
# n개씩 나눠 2차원 배열로 변경

# for문, if문
def solution(num_list, n):
    answer = []
    cnt = 0
    temp = []
    for num in num_list:
        temp.append(num)
        cnt += 1
        if cnt == n:
            answer.append(temp)
            temp = []
            cnt = 0
    return answer

# 컴프리헨션
def solution(num_list, n):
    return [num_list[idx - n : idx] for idx in range(n, len(num_list) + 1, n)]

# numpy
import numpy

def solution(num_list, n):
    list = numpy.array(num_list).reshape(-1, n)
    return list.tolist()