# 25024

# 어느 날 시계를 본 경근이는 시간이 8시 14분인 것을 보고 놀랐다
# 왜냐하면 그의 생일은 8월 14일이기 때문이다
# 그리고 이 경험을 바탕으로 다음과 같은 문제를 만들었다
# 두 정수 x, y가 주어질 때 x시 y분으로 읽는 것이 가능한지의 여부를 판단하면서
# x월 y일로 읽는 것이 가능한지의 여부를 판단하라
# 시는 0시에서 23시까지, 분은 0분에서 59분까지가 유효하며
# 월은 1월부터 12월까지가 유효하다
# 1, 3, 5, 7, 8, 10, 12월은 1일에서 31일까지가 유효하고
# 4, 6, 9, 11월은 1일에서 30일까지가 유효아며
# 2월은 1일에서 29일까지가 유효하다

# 첫번째 줄에 테스트 케이스의 개수 T가 주어진다
# 각 테스트 케이스는 한 줄로 구성되어
# 두 정수 x, y가 공백 하나로 구분되어 주어진다

# 각 테스트 케이스마다 두 문자열을 공백 하나로 구분하여 출력
# 첫번째 문자열은 두 정수 x, y를 x시 y분으로 읽는 것이 가능하면 'Yes'
# 가능하지 않으면 'No'여야 한다
# 두번째 문자열은 두 정수 x, y를 x월 y일로 읽는 것이 가능하면 'Yes',
# 가능하지 않으면 'No'여야 한다
# 따옴표는 제외하고 출력되어야 하며
# 정답과 맞지 않더라도 두 문자열이 모두 출력되어야 제대로 된 채점이 가능하다



# 1,
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    time = 'Yes' if x < 24 and y < 60 else 'No'
    days = 'No'
    if 0 < x < 13:
        if x in [1, 3, 5, 7, 8, 10, 12] and 0 < y < 32:
            days = 'Yes'
        elif x in [4, 6, 9, 11] and 0 < y < 31:
            days = 'Yes'
        elif x == 2 and 0 < y < 30:
            days = 'Yes'
    print(time, days)
# 60ms
# sys를 사용하지 않으면 912ms



# 2.
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    li = []
    x, y = map(int, sys.stdin.readline().split())
    li.append('Yes' if x < 24 and y < 60 else 'No')
    if x in [1, 3, 5, 7, 8, 10, 12] and 0 < y < 32:
        li.append('Yes')
    elif x in [4, 6, 9, 11] and 0 < y < 31:
        li.append('Yes')
    elif x == 2 and 0 < y < 30:
        li.append('Yes')
    elif len(li) < 2:
        li.append('No')
    print(' '.join(li))
# 60ms
# sys를 사용하지 않으면 916ms