# 10816
# 숫자 카드는 정수 하나가 적혀져 있는 카드다
# 숫자 카드 N개를 가지고 있으며 정수 M개가 주어졌을 때
# 이 수가 적혀있는 숫자 카드를 몇 개 가지고 있는지 구하라

# 첫째 줄에 가지고 있는 숫자 카드의 수 N이 주어진다
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다
# 셋째 줄에는 M이 주어진다
# 넷째 줄에는 몇개 가지고 있는 숫자 카드인지 구해야 할
# M개의 정수가 주어지며 이 수는 공백으로 구분되어 있다

# 첫째 줄에 입력으로 주어진 M개의 수에 대해서
# 각 수가 적힌 숫자 카드를 몇 개 가지고 있는지를 공백으로 구분해 출력

# 출력 예시
# 3 0 0 1 2 0 0 2

import sys
sys.stdin = open('숫자카드2.txt')

#* 가지고 있는 숫자 카드의 수
N = int(input())
#* 숫자 카드에 적혀있는 정수
cardNumber = (list(map(int, input().split())))

M = int(input())
number = (list(map(int, input().split())))

index, m_dic = 0, {}

#* number를 정렬하고 number의 길이만큼 for문을 돌림
#? sort 대신 sorted를 사용하는 이유
#? sort는 반환값이 없이 None 원래 리스트를 정렬
#? sorted는 정렬한 리스트를 반환하는 대신 원래 리스트를 변경하지 않음
#? for문에서 sort로 실행하면 Error
for m in sorted(number):
    count = 0
    #* 만약 m_dic에 m이 없다면
    if m not in m_dic:
        #* cardNumber의 길이보다 index가 작을 때
        while index < len(cardNumber):
            #* 만약 cardNumber[index]가 m과 같다면
            if m == cardNumber[index]:
                #* count와 index에 1씩 추가
                count += 1
                index += 1
            #* m이 cardNumber[index]보다 크다면
            elif m > cardNumber[index]:
                #* indexd에만 1 추가
                index += 1
            else:
                break
        #* m_dic의 m번째 인덱스에 count 값을 넣음
        m_dic[m] = count

print(' '.join(str(m_dic[m]) for m in number))