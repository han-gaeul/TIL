# 2495
# 여덟 자리의 양의 정수가 주어질 때
# 그 안에서 연속하여 같은 숫자가 나오는 것이 없으면 1 출력
# 같은 숫자가 연속해서 나오면 구간 중 가장 긴 것의 길이를 출력

# 첫째 줄부터 셋째 줄까지 각 줄에 하나씩 세 개의 여덟 자리 정수가 주어진다

import sys
sys.stdin = open('연속구간.txt')

for _ in range(3):
    number = list(input())

    max_  =1
    count = 1

    for i in range(1, len(number)):
        if number[i] == number[i -1]:
            count += 1
        else:
            max_ = max(count, max_)
            count = 1
    max_ = max(count, max_)
    print(max_)