# 첫째 줄에 A, B, C가 순서대로 주어진다

# 첫째 줄에 (A+B)%C
# 둘째 줄에 ((A%C) + (B%C))%C
# 셋째 줄에 (A×B)%C
# 넷째 줄에 ((A%C) × (B%C))%C를 출력


A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)