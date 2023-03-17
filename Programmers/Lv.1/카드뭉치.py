# 코니는 영어 단어가 적힌 카드 뭉치 두 개를 선물로 받았다
# 코니는 다음과 같은 규칙으로 카드에 적힌 단어들을 사용해
# 원하는 순서의 단어 배열을 만들 수 있는지 알고 싶다
# 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용한다
# 한 번 사용한 카드는 다시 사용할 수 없다
# 카드를 사용하지 않고 다음 카드로 넘어갈 수 없다
# 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없다
# 예를 들어 첫번째 카드 뭉치에 순서대로 ['i', 'drink', 'water'],
# 두번째 카드 뭉치에 순서대로 ['want', 'to']가 적혀있을 때,
# ['i', 'want', 'to', 'drink', 'water'] 순서의 단어 배열을
# 만들려고 한다면, 첫번째 카드 뭉치에서 i를 사용한 후 두번째
# 카드 뭉치에서 want와 to를 사용하고 첫번째 카드 뭉치에
# drink와 water를 차례대로 사용하면 원하는 순서의 단어 배열을
# 만들 수 있다
# 문자열로 이루어진 배열 cards1, cards2와 원하는 단어 배열 goal이
# 매개변수로 주어질때, cards1과 cards2에 적힌 단어들로 goal을
# 만들 수 있다면 Yes를, 만들 수 없다면 No를 return

from collections import deque

def solution(cards1, cards2, goal):
    # deque를 이용해 각각 큐로 변환
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    # goal의 모든 단어 탐색
    for word in goal:
        # cards1이 비어있지 않고,
        # 현재 단어가 덱의 맨 앞에 있는 단어와 일치할 경우
        if cards1 and word == cards1[0]:
            # 맨 앞에 있는 단어를 뺌
            cards1.popleft()
        elif cards2 and word == cards2[0]:
            cards2.popleft()
        # 현재 단어가 두 덱의 맨 앞에 있는 단어와 일치하지 않는 경우
        else:
            return 'No'
    return 'Yes'



# cards1과 cards2에서 단어를 뽑아 goal을 만들 수 있는지
# 여부를 판단하여 결과를 반환하는 문제이다.
# 먼저 cards1과 cards2를 deque로 변환한다. deque는 스택과
# 큐의 기능을 모두 갖춘 자료구조이다. 이 코드에서는 큐로 사용했다.
# 이후 for문을 이용해 goal의 모든 단어를 하나씩 탐색한다.
# 우선 cards1과 cards2가 비어있지 않은지 검사한다. 두 리스트는
# deque 자료형이므로 덱의 맨 앞에 있는 요소를 가져오기 위해서
# popleft 메소드를 사용해 덱의 맨 왼쪽 요소를 삭제하고 반환한다.
# 현재 단어가 덱의 맨 앞에 있는 단어와 일치한다면 그 덱에서
# 해당 단어를 빼낸다. 만약 현재 단어가 덱의 맨 앞에 있는 단어와
# 일치하지 않으면 그 다음 덱의 맨 앞에 있는 단어와 비교한다.
# 현재 단어가 두 덱의 맨 앞에 있는 단어와 일치하지 않으면
# goal을 만들 수 없으므로 No를 반환하고 함수를 종료한다.
# 이 과정을 모두 거쳐 goal을 만들 수 있다면 Yes를 반환한다.