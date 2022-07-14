a =  input()

a = int(a)

if a < 0:
    if a % 2 == 0:
        print('A')
        # 주의할 점
        # 변수 A 와 문자열 'A' / "A"는 의미가 완전히 다르다
    else:
        print('B')
else:
    if a % 2 == 0:
        print('C')
    else:
        print('D')


# 조건/선택 실행 구조 안에 다시 조건/선택 실행 구조를 '중첩' 할 수 있음
# 또 중첩된 조건은
# if (n < 0) and (n % 2 == 0):
#   print('A)
# 와 같이 논리 연산자(not, and, or)를 이용해 합쳐 표현 가능
# 비교 연산(<, >, <=, >=, ==, !=)의 계산 결과는 True 또는 False의 불린(booean) 값이고
# 불린 값들 사이의 논리 연산의 결과도 True 또는 False의 불린 값이다.