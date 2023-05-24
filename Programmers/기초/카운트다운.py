# 정수 start와 end가 주어질 때
# start에서 end까지 1씩 감소하는 수들을 차례로 담은
# 리스트 return

def solution(start, end):
    ans = []
    while start >= end:
        ans.append(start)
        start -= 1
    return ans