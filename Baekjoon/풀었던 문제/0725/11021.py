# 두 정수 A, B를 입력받은 다음
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력
# 예 : Case #1: 2

T = int(input())
    
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    num = A + B
    print('Case #{}: {}'.format(test_case, num))