# 길이가 n이고 "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 return
# 예를 들어 n이 4이면 "수박수박"을 반환하고
# 3이라면 "수박수"를 반환

def solution(n):
    return ('수박' * n)[:n]


def solution(n):
    answer = '수박' * 5000
    return answer[:n]


def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer