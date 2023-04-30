# 정수 start와 end가 주어질 때
# start부터 end까지의 숫자를 차례로 담은 리스트를 반환

def solution(start, end):
    ans = []
    for i in range(start, end + 1):
        ans.append(i)
    return ans