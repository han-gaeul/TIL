# 수많은 마라톤 선수들이 마라톤에 참여했다
# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주했다
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와
# 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때
# 완주하지 못한 선수의 이름을 return


# 동명이인의 경우 검증하지 못함
def solution(participant, completion):
    answer = []
    for i in participant:
        if i not in completion:
            answer.append(i)
    return ''.join(answer)



def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    # 완주자 배열을 끝까지 반복해도 다른 것을 찾지 못하면
    # 미완주자는 참가자 배열의 맨 마지막에 있을 것이기 때문에
    # -1 인덱스로 반환
    return participant[-1]



import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# collections
# 배열에 들어있는 요소의 개수를 파악해서 딕셔너리 형태로 변환
# {'요소 이름' : '개수'}



def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

# zip 함수
# 같은 인덱스끼리 짝을 지음