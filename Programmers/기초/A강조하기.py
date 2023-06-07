# 문자열 myString이 주어진다
# myString에서 알파벳 a가 등장하면 전부 A로 변환하고,
# A가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return

def solution(myString):
    return myString.lower().replace('a', 'A')