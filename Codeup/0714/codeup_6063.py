a, b = input().split()
a = int(a) # 변수 a에 저장되어 있는 값을 정수로 바꾸어 다시 변수 a에 저장
b = int(b)
c = (a if (a>=b) else b)
print(c)

# 3항연산
# x if C else y 의 형태로 작성
# C True 또는 False를 평가할 조건식 또는 값
# x C의 평가 결과가 True일 때 사용할 값
# y C의 평가 결과가 True가 아닐 때 사용할 값

# 조건식 또는 값이 True 이면 x 값이 사용되고
# True가 아니면 y 값이 사용되도록 하는 코드