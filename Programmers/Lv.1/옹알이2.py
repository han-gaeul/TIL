# 머쓱이는 태어난지 11개월 된 조카를 돌보고 있다
# 조카는 아직 'aya', 'ye', 'woo', 'ma' 네 가지 발음과 네 가지
# 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서
# 같은 발음을 하는 것을 어려워한다. 문자열 배열 babbling이
# 매개변수로 주어질 때 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return


def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya', 'ye', 'woo', 'ma']:
            # 연속된 발음이 없다면
            if j * 2 not in i:
                #발음 가능한 단어를 공백으로 바꿈
                i = i.replace(j, ' ')
        # 공백을 제외하고 아무것도 없다면
        if len(i.strip()) == 0:
            answer += 1
    return answer