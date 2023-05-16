# 문자열 배열 intStrs와 정수 k, s, l이 주어진다
# intStrs의 원소는 숫자로 이루어져 있다
# 배열 intStrs의 각 원소마다 s번 인덱스에서 시작하는 길이
# l짜리 부분 문자열을 잘라내 정수로 변환한다
# 이때 변환한 정수값이 k보다 큰 값들을 담은 배열을 return

def solution(intStrs, k, s, l):
    ans = []
    for string in intStrs:
        substr = string[s:s+l]
        num = int(substr)
        if num > k:
            ans.append(num)
    return ans