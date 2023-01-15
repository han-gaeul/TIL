# 두 배열이 얼마나 유사한지 확인해보려고 한다
# 문자열 배열 s1과 s2가 주어질 때
# 같은 원소의 개수를 return

def solution(s1, s2):
    return len(set(s1).intersection(s2))


# set(x).intersection(y)
# a = [2, 3, 4]
# b = [4, 5, 6]
# answer = set(a).intersection(b)
# 중복된 값을 반환