# 문자열 배열 strArr가 주어진다
# 모든 원소가 알파벳으로만 이루어져 있을 때, 배열에서 홀수번째
# 인덱스의 문자열은 모든 문자를 대문자로, 짝수번째 인덱스의
# 문자열은 모든 문자를 소문자로 바꿔서 return

def solution(strArr):
    res = []
    for i in range(len(strArr)):
        if i % 2 == 0:
            res.append(strArr[i].lower())
        else:
            res.append(strArr[i].upper())
    return res