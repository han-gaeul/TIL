# 문자열 배열 strArr가 주어진다
# 배열 내의 문자열 중 ad라는 부분 문자열을 포함하고 있는
# 모든 문자열을 제거하고 남은 문자열을 순서를 유지하여 배열로 return

def solution(strArr):
    res = []
    for i in strArr:
        if 'ad' not in i:
            res.append(i)
    return res