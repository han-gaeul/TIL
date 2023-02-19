# 4458

# 문장을 읽은 뒤 줄의 첫 글자를 대문자로 바꿔라

# 첫째 줄에 줄의 수 N이 주어진다
# 다음 N개의 줄에는 문장이 주어진다
# 각 문자에 들어있는 글자의 수는 30을 넘지 않는다
# 모든 줄의 첫 번째 글자는 알파벳이다

# 각 줄의 첫글자를 대문자로 바꾼뒤 출력

N = int(input())
for _ in range(N):
    sentence = input()
    sentence = sentence[0].upper() + sentence[1:]
    print(sentence)