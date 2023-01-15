# 머쓱이는 행운의 숫자 7을 가장 좋아한다
# 정수 배열 array가 매개변수로 주어질 때
# 7이 총 몇 개 있는지 return

def solution(array):
    answer = ''
    for i in array:
        answer += str(i)
    return answer.count('7')