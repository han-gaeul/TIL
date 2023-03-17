# 두 문자열 s와 skip, 그리고 자연수 index가 주어질 때, 다음 규칙에 따라
# 문자열을 만들려한다. 암호의 규칙은 다음과 같다
# 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꾼다
# index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아간다
# skip에 있는 알파벳은 제외하고 건너뛴다
# 예를 들어 s = aukks, skip = wbqd, index = 5 일때, a에서 5만큼 뒤에
# 있는 알파벳은 f지만 [b, c, d, e, f]에서 b와 d는 skip에 포함되므로
# 세지 않는다. 따라서 b, d를 제외하고 a에서 5만큼 뒤에 있는 알파벳은
# [c, e, f, g, h] 순서에 의해 h가 된다. 나머지 ukks 또한 위 규칙대로
# 바꾸면 appy가 되며 결과는 happy가 된다
# 두 문자열 s와 skip, 그리고 자연수 index가 매개변수로 주어질 때
# 위 규칙대로 s를 변환한 결과를 return

import re

def solution(s, skip, index):
    # skip에 있는 알파벳을 |로 연결해 정규식 패턴을 만듦
    skip = '|'.join([x for x in skip])
    # skip에 있는 알파벳을 제외한 알파벳을
    # 연속해서 3번 반복한 문자열을 만듦
    alpha = re.sub(skip, '', 'abcdefghijklmnopqrstuvwxyz') * 3
    # s에서 각 알파벳을 index만큼 이동한 알파벳으로 변환하여 반환
    return ''.join([alpha[alpha.index(i) + index] for i in s])



# 이 문제는 주어진 문자열 s와 skip, 자연수 index를 이용해 s를 
# 변환하는 문제이다. skip에 있는 알파벳은 건너뛰고, s의 각 알파벳을
# index만큼 이동한 알파벳으로 바꾸는 것이 목표이다.
# 이를 위해서 정규식을 이용해 skip에 포함된 알파벳을 건너뛰고
# 나머지 알파벳으로 구성된 문자열을 alpha에 저장한다
# 그리고 문자열 alpha를 3번 반복하여 만든 이유는, index만큼
# 이동한 알파벳을 구하기 위해서이다. 예를 들어, alpha가
# 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'라면
# alpha[0 + index]는 index만큼 이동한 a가 된다
# 또한, alpha[-1 + index]는 z에서 index만큼 이동한 알파벳이 된다
# 마지막으로 s에서 각 알파벳을 index만큼 이동한 알파벳으로
# 변환하여 문자열을 만들어 반환한다.