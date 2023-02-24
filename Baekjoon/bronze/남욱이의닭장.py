# 11006

# 계란집을 운영하는 남욱이는 매일 닭장에서 달걀을 수거해간다
# 어느날 닭장에 들어가보니 일부 닭의 다리가 하나씩 사라졌다
# 남욱이는 얼마나 많은 닭들이 한 다리를 잃었는지 알고 싶었지만
# 닭이 너무 많아 셀수 없었고 대신 모든 닭의 다리수를 셌다
# 고민하는 남욱이를 위해 모든 닭의 다리수의 합과 닭의 수를 가지고 해결하자

# 첫째 줄에 총 테스트 케이스의 수 T가, 둘째 줄부터 T + 1번째줄까지
# 매 줄마다 모든 닭의 다리수의 합 N과 닭의 수 M이 공백을 간격으로 입력된다

# 테스트 케이스마다 한줄에 다리가 잘린 닭의 수 U와 멀쩡한 닭의 수 T를 공백을 간격으로 출력

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    U = 2 * M - N
    print(U, M - U)



# '한 다리가 잘린 닭의 수(U)' = '닭의 수(M) * 2 - 모든 닭의 다리수의 합(N)'
# '멀쩡한 닭의 수(T)' = '닭의 수(M) - 한 다리가 잘린 닭의 수(U)'