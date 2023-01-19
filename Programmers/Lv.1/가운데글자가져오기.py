# 단어 s의 가운데 글자를 return
# 단어의 길이가 짝수라면 가운데 두 글자를 return

def solution(s):
    return s[(len(s) - 1) // 2 : len(s) // 2 + 1]