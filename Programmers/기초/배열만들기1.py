# 정수 n과 k가 주어졌을 때, 1 이상 n 이하의 정수 중에서
# k의 배수를 오름차순으로 저장한 배열을 return

def solution(n, k):
    ans = []
    for i in range(1, n + 1):
        if i % k == 0:
            ans.append(i)
    return ans