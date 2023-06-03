# 정수 배열 arr가 주어진다. arr의 각 원소에 대해 값이
# 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면
# 2를 곱한다. 그 결과인 정수 배열을 return

def solution(arr):
    res = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            res.append(i // 2)
        elif i < 50 and i % 2 != 0:
            res.append(i * 2)
        else:
            res.append(i)
    return res