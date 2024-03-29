# 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어진다
# a와 b의 내적을 return
# 이때 a와 b의 내적은 a[0] * b[0] + a[1] * b[1] + ... + a[n - 1] * b[n -1] 이다
# n은 a, b의 길이

def solution(a, b):
    return sum([x * y for x, y in zip(a, b)])



def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer