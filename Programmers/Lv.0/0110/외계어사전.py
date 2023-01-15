# PROGRAMMERS-962 행성에 불시착한 우주비행사
# 머쓱이는 외계행성의 언어를 공부하려고 한다
# 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어진다
# spell에 담긴 알파벳을 한 번씩만 모두 사용한 단어가
# dic에 존재한다면 1, 존재하지 않는다면 2를 return

def solution(spell, dic):
    spell = {i: 0 for i in spell}
    for x in dic:
        if len(x) == len(spell):
            for y in x:
                if y in spell:
                    spell[y] += 1
                else:
                    break
            if len(set(spell.values())) == 1 and sum(set(spell.values())) == 1:
                return 1
            spell = {i: 0 for i in spell}
    return 2