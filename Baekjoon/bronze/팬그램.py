# 5704

# 팬그램은 알파벳의 모든 글자들을 사용해서 만든 문장이다
# 'the quick brown fox jumps over a lazy dog'과
# 'jackdaws loves my big sphinx of quzrtz'은 팬그램이다
# 문장이 주어졌을 때 팬그램인지 아닌지 알아내자

# 입력은 여러 테스트 케이스로 이루어져 있다
# 각 테스트 케이스는 많아야 200글자로 이루어져 있는 문장이다
# 단어는 공백 하나로 구분되어 있다. 또 단어는 알파벳 소문자로만 이루어져 있다
# 입력의 마지막 줄에는 별표가 하나 주어진다

# 각 테스트 케이스에 대해서 입력으로 주어진 문장이 팬그램이라면 'Y', 아니면 'N'를 출력


# 1.
from collections import Counter

while True:
    sentence = input()
    if sentence == '*':
        break
    sentence = sentence.replace(' ', '')
    cnt = Counter(sentence)
    if len(cnt.keys()) == 26:
        print('Y')
    else:
        print('N')



# 2. 
while True:
    sentence = input()
    pangram = 'Y'
    if sentence == '*':
        break
    else:
        for alphabet in range(97, 123):
            if sentence.find(chr(alphabet)) == -1:
                pangram = 'N'
                break
        print(pangram)