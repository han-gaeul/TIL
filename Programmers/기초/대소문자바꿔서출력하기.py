# 영어 알파벳으로 이루어진 문자열 str이 주어진다
# 각 알파젯을 대문자는 소문자로, 소문자는 대문자로 변환해서 출력

str = input()
answer = []
for i in str:
    if i.isupper():
        answer.append(i.lower())
    if i.islower():
        answer.append(i.upper())
print(*answer, sep='')