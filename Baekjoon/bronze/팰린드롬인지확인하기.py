# 10988

# 알파벳 소문자로만 이루어진 단어가 주어진다
# 이때 이 단어가 팰린드롬인지 아닌지 확인하라
# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을때 똑같은 단어를 말한다
# level, noon은 팰린드롬이고 baekjoon, online, judge는 팰린드롬이 아니다

# 첫째 줄에 단어가 주어진다

# 첫째 줄에 팰린드롬이면 1, 아니면 0 출력

word = list(str(input()))
if list(reversed(word)) == word:
    print(1)
else:
    print(0)