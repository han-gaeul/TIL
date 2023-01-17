# 17388
# 숭고한 알고리즘 캠프의 구성원인 숭실대학교(Soongsil University),
# 고려대학교(Korea University), 한양 대학교(Hanyang University)
# 세 대학의 참여도를 수치화하였다
# 세 대학교의 참여도의 합이 100 이상이면
# 일처리가 잘 되고 있기에 안심할 수 있지만
# 100 미만이면 참여도가 가장 낮은 대학의 동아리에게
# 무언의 압박을 넣을 예정이다

# 첫 번째 줄에 세 대학의 참여도를 의미하는
# 세 자연수 S, K, H가 공백으로 구분되어 주어진다
# 세 대학의 참여도는 모두 다르다

# 첫 번째 줄에 일처리가 잘 되고 있어 압박이 필요 없으면 OK 출력
# 그 외에는 첫 번째 줄에 압박이 필요한 동아리가 속한 대학의
# 영문 이름의 첫 단어를 출력

import sys
sys.stdin = open('와글와글숭고한.txt')

#* 내 풀이
S, K, H = map(int, input().split())
sum_= S + K + H

if sum_ >= 100:
    print('OK')
elif sum_ < 100:
    dic = {'Soongsil' : S, 'Korea' : K, 'Hanyang' : H}
    print(min(dic, key=dic.get))

#! ----------------------------------------------------------

#* 구글링
S, K, H = map(int, input(). split())
dic = {S : 'Soongsil', K : 'Korea', H : 'Hanyang'}

if sum(dic) >= 100:
    print('OK')
else:
    print(dic[min(dic)])
