# 1076
# 전자 제품에는 저항이 들어간다
# 저항은 색 3개를 이용해 그 저항이 몇 옴인지 나타낸다
# 처음 색 2개는 저항의 값이고 마지막 색은 곱해야 하는 값이다
# 색	값	곱
# black	0	1
# brown	1	10
# red	2	100
# orange	3	1,000
# yellow	4	10,000
# green	5	100,000
# blue	6	1,000,000
# violet	7	10,000,000
# grey	8	100,000,000
# white	9	1,000,000,000
# 예 : 저항의 색이 yellow, violet, red 라면 저항의 값은 4,700

# 첫째 줄에 첫 번째 색, 둘째 줄에 두 번째 색, 셋째 줄에 세 번째 색이 주어진다
# 저항의 저항값을 계산하여 첫째 줄에 출력

import sys
sys.stdin = open('저항.txt')

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
first = color.index(input())
second = color.index(input())
third = color.index(input())
print(int(str(first) + str(second)) * (10 ** third))