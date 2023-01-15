# 머쓱이는 태어난지 6개월 된 조카를 돌보고 있다
# 조카는 아직 'aya', 'ye', 'woo', 'ma' 네 가지 발음을
# 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못한다
# 문자열 배열 babbling이 매개변수로 주어질 때
# 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return

from itertools import permutations

def solution(babbling):
    answer = 0
    speek = ['aya', 'ye', 'woo', 'ma']
    word = []

    for i in range(1, len(speek) + 1):
        # 모든 경우의 수를 저장
        for j in permutations(speek, i):
            word.append(''.join(j))
    
    for i in babbling:
        if i in word:
            answer += 1
    return answer


# permutations 순열 함수
# a = ['a', 'b', 'c', 'd']
# p = list(permutations(a, 2))
# p = [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
# 순열을 이용해 모든 경우의 수를 저장
# 서로 다른 n개 중 r개를 골라 순서를 정해 나열하는 가짓수
# 순서를 고려하기 때문에 ('a', 'b')와 ('b', 'a')는 다른 것