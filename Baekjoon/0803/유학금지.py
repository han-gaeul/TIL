# 백준 2789
# 한 나라에서 가장 공부를 잘하는 학생들은 모두 다른 나라로 유학을 감
# 정부는 최고의 학생들이 자꾸 유학을 가는게 불쾌
# 학생들이 가장 많이 유학을 가는 대학교는 영국의 캠브리지
# 정부는 인터넷 검열을 통해 해외로 나가는 이메일 내용 중 일부를 삭제
# 이메일의 각 단어 중에서 CAMBRIDGE에 포함된 알파벳은 모두 지움
# 이메일에 LOVA라는 단어가 있다면
# A는 CAMBRIDGE에 포함된 알파벳이기 때문에
# 받아보는 사람은 LOV로 받는다

# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다
# 단어에서 CAMBRIDGE에 포함된 알파벳을 모두 지운뒤 출력

import sys
sys.stdin = open('유학금지.txt', 'r')

camb = 'CAMBRIDGE'
word = list(input())

for i in camb:
    for j in range(len(word)):
        if i == word[j]:
            word[j] = ''

for i in word:
    print(i, end = '')