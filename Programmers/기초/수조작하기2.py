# 정수 배열 numLog가 주어진다
# 처음에 numLog[0]에서부터 시작해 w, a, s, d로 이루어진
# 문자열을 입력으로 받아 순서대로 다음과 같은 조작을 한다
# w : 수에 1을 더한다
# s : 수에 1을 뺀다
# d : 수에 10을 더한다
# a : 수에 10을 뺀다
# 그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이
# numLog이다. 즉, numLog[i]는 numLog[0]로부터 총 i번의
# 조작을 가한 결과가 저장되어 있다
# 주어진 정수 배열 numLog에 대해 조작을 위해 입력받은
# 문자열을 반환

def solution(numLog):
    ans = ''
    for i in range(len(numLog) - 1):
        diff = numLog[i + 1] - numLog[i]
        if diff == 1:
            ans += 'w'
        elif diff == -1:
            ans += 's'
        elif diff == 10:
            ans += 'd'
        elif diff == -10:
            ans += 'a'
    return ans