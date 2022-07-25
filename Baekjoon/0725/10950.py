# 두 정수 A, B를 입력받은 다음
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 
# 각 줄에 A와 B가 주어진다.

T = int(input())
    
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    print(A + B)