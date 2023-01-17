# 백준 2789
# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다
# 단어에서 CAMRIDGE에 포함된 알파벳을 모두 지운 뒤 출력

camb = 'CAMBRIDGE'
word = list(input())

for i in camb:
    for j in range(len(word)):
        if i == word[j]:
            word[j] = ''

for i in word:
    print(i, end = '')