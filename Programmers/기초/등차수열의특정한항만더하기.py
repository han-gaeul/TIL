# 두 정수 a, d와 길이가 n인 boolean 배열 included가 주어진다
# 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 
# i + 1항을 의미할 때, 이 등차수열의 1항부터 n항까지
# included가 true인 항들만 더한 값을 반환

def solution(a, d, included):
    res = 0
    for i in range(len(included)):
        if included[i]:
            res += a + d * i
    return res