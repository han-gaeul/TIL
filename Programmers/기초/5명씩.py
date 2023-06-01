# 최대 5명씩 탑승가능한 놀이기구를 타기 위해 줄을 서있는
# 사람들의 이름이 담긴 문자열 리스트 names가 주어질 때
# 앞에서부터 5명씩 묶은 그룸의 가장 앞에 서 있는 사람들의
# 이름을 담은 리스트를 return
# 마지막 그룹이 5명이 되지 않더라도 가장 앞에 있는 사람의
# 이름을 초함한다

def solution(names):
    res = []
    group_cnt = (len(names) + 4) // 5
    for i in range(group_cnt):
        group = names[i * 5 : (i + 1) * 5]
        res.append(group[0])
    return res