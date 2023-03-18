# JadenCase란 모든 단어의 첫 문자가 대문자이고
# 그 외의 알파벳은 소문자인 문자열이다
# 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은
# 소문자로 쓰면 된다.
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼
# 문자열을 return

def solution(s):
    # 문자열을 공백으로 나눠 단어 리스트로 변환
    words = s.split(' ')
    for i in range(len(words)):
        # 각 단어의 첫글자를 대문자로 변환
        words[i] = words[i].capitalize()
    return ' '.join(words)



# capitalize()
# 문자열의 첫글자는 대문자로, 나머지는 소문자로 변환