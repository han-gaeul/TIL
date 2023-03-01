# 5430

# 선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다
# AC는 정수 배열에 연산을 하기 위해 만든 언어이다
# 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다
# 함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고 D는 첫번째 수를 버리는 함수이다
# 배열이 비어있는데 D를 사용한 경우 에러가 발생한다
# 함수는 조합해서 한 번에 사용할 수 있다.
# 예를 들어 "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다
# 예를 들어 'RDD'는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다
# 배열의 초기값과 수행할 함수가 주어졌을 때 최종 결과를 구하라

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다
# 각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다
# 다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다
# 다음 줄에는 [x1, ..., xn]과 같은 형태로 배열에 들어있는 정수가 주어진다
# 전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다

# 각 테스트 케이스에 대해서 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력
# 만약 에러가 발생한 경우 error 출력

import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    command = sys.stdin.readline().strip()
    n = int(input())
    n_li = deque(sys.stdin.readline().strip()[1:-1].split(','))
    # 에러 발생 여부를 나타내는 변수 선언
    error = False
    # 배열이 뒤집혀있는지 여부를 나타내는 변수 선언
    reverse = False
    # 배열의 크기가 0이라면 빈 deque를 생성
    if n == 0:
        n_li = deque()
    for com in command:
        if com == 'R':
            # 배열이 뒤집혀있다면
            if reverse:
                # 원래대로 뒤집음
                reverse = False
            # 배열이 원래대로라면
            else:
                # 배열을 뒤집은 상태로 저장
                reverse = True
        else:
            # deque에 원소가 있고 뒤집혀있다면
            if n_li:
                if reverse:
                    # 오른쪽 끝에 있는 원소 제거
                    n_li.pop()
                # 배열이 원래대로라면
                else:
                    # 왼쪽 끝에 있는 원소 제거
                    n_li.popleft()
            # deque에 원소가 없다면
            else:
                # 에러 발생
                error = True
                break
    if error:
        print('error')
    elif reverse:
        n_li.reverse()
        print('[' + ','.join(n_li) + ']')
    else:
        print('[' + ','.join(n_li) + ']')