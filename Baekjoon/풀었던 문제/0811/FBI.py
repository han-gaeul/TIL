# 2857
# 5명의 요원 중 FBI 요원을 찾는 프로그램
# FBI 요원은 요원의 첩보원명에 FBI가 들어있다

# 5개 줄에 요원의 첩보원명이 주어진다
# 첩보원명은 알파벳 대문자, 숫자 0 ~ 9
# 대시(-)로만 이루어져 있으며 최대 10글자

# 첫째 줄에 FBI 요원을 출력
# 이때 해당하는 요원이 몇 번째 입력인지를 공백으로 구분하며
# 오름차순으로 출력한다
# 만약 FBI 요원이 없다면 'HE GOT AWAY!' 출력

import sys
sys.stdin = open('FBI.txt')

nameList = []

for i in range(1, 6):
    name = input()

    if 'FBI' in name:
        nameList.append(i)

if nameList:
    print(*nameList)
else:
    print('HE GOT AWAY!')

#? print에서 쓰는 *는 unpaking
#? 리스트나 튜플 앞에 *(애스터리스크)를 붙여
#? 인자들을 일일히 넘기는 효과
#? 즉 리스트의 포장을 풀어준다