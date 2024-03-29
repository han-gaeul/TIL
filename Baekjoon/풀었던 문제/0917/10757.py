# 두 정수 A와 B를 입력받은 다음 A + B를 출력

# 첫째 줄에 A와 B가 주어진다

# 첫째 줄에 A + B를 출력

A, B = map(int, input().split())
print(A + B)

# C언어의 경우 자료형에 따른 메모리가 한정되어 있기 때문에 에러 발생
# 파이썬의 경우 오버플로우가 없기 때문에 에러가 나지 않는다
# 파이썬 언어 자체적으로 BigInt를 지원하기 때문에
# 문제없이 연산이 가능하다