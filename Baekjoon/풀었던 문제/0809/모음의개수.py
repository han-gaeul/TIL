# 1264
# 영문 문장을 입력받아 모음의 개수를 세는 프로그램 작성
# 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자

# 입력은 여러 개의 테스트 케이스로 이루어져 있으며
# 각 줄마다 영어 대소문자 ',', '.', '!', '?', 공백으로 이루어진 문장이 주어진다
# 입력의 끝에는 한 줄에 '#' 한 글자만 주어진다

# 출력 예시
# 7
# 14
# 9

import sys
sys.stdin = open('모음의개수.txt')

while True:
    sentence = input()

    #* 마지막 줄에 있는 '#'를 만나면 멈춤
    if sentence == '#':
        break

    count = 0

    #* for문을 돌면서 sentence안에 있는 값을 하나씩 i에 담음
    for i in sentence:
        #* 만약 i 안에 'aeiouAEIOU'가 있다면 count에 1 추가
        if i in 'aeiouAEIOU':
            count += 1
    print(count)