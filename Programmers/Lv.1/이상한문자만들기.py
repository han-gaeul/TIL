# 문자열 s는 한 개 이상의 단어로 구성되어 있다
# 각 단어는 하나 이상의 공백 문자로 구분되어 있다
# 각 단어의 짝수번째 알파벳은 대문자로,
# 홀수번째 알파벳은 소문자로 바꾼 문자열을 return

def solution(s):
    s = s.split(' ')
    answer = []
    for i in s:
        new = ''
        for j in range(len(i)):
            new += i[j].upper() if j % 2 == 0 else i[j].lower()
        answer.append(new)
    return ' '.join(answer)