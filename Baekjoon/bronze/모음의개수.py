# 10987

# 알파벳 소문자로만 이루어진 단어가 주어진다
# 이때 모음(a, e, i, o, u)의 개수를 출력

# 첫째 줄에 단어가 주어진다
# 단어는 알파벳 소문자로만 이루어져 있다

# 첫쨰 줄에 모음의 개수를 출력

sentence = input()
cnt = sum(1 for i in sentence if i in 'aeiou')
print(cnt)