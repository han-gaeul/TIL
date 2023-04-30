# 정수 l과 r이 주어졌을 때 l 이상 r 이하의 정수 중에서
# 숫자 0과 5로만 이루어진 모든 정수를 오름차순으로
# 저장한 배열을 반환
# 만약 그러한 정수가 없다면 -1이 담긴 배열 반환

def solution(l, r):
    ans = []
    for num in range(l, r + 1):
        str_num = str(num)
        if all(x in '05' for x in str_num):
            ans.append(num)
    if not ans:
        return [-1]
    return ans