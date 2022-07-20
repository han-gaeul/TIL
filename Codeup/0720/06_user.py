import lotto_class

lotto = lotto_class.Lotto()
lotto.generate_lotto()
print(lotto.numbers)
print(lotto.get_money([1, 2, 3, 4, 5, 6]))

# lotto 인스턴스로 속성 볼 수 있고(numberes)
# 내가 생성도 하고 확인(get_money)도 가능함