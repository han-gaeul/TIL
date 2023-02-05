# 5355

# 겨울 방학에 달에 다녀온 상근이는 여름 방학 때는 화성이 다녀올 예정
# 화성에서는 지구와는 조금 다른 연산자 @, %, #을 사용한다
# @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다
# 따라서 화성에서는 수학 식의 가장 앞에 수가 하나 있고 그 다음 연산자가 있다

# 첫쨰 줄에 테스트 케이스의 개수 T가 주어진다
# 다음 줄에는 화성 수학식이 한 줄에 하나씩 주어진다
# 연산자는 최대 3개 주어진다

# 각 테스트 케이스에 대해서 화성 수학싱의 결과를 계산한 다음
# 소수점 둘째 자리까지 출력

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    list_ = list(sys.stdin.readline().split())
    # 리스트에서 숫자만 실수형으로 뽑아냄
    num = float(list_.pop(0))
    for i in range(len(list_)):
        if list_[i] == '@':
            num *= 3
        elif list_[i] == '%':
            num += 5
        elif list_[i] == '#':
            num -= 7
    print('{:.2f}'.format(num))