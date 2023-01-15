# 머쓱이네 옷가게는 10만원 이상 사면 5%
# 30만원 이상 사면 10%
# 50만원 이상 사면 20%를 할인 해준다
# 구매한 옷의 가격 price가 주어질때 지불해야 할 금액을 return

# if문
def solution(price):
    if 100000 <= price and price < 300000:
        return int(price * 0.95)
    elif 300000 <= price and price < 500000:
        return int(price * 0.9)
    elif 500000 <= price:
        return int(price * 0.8)
    else:
        return int(price)

# 딕셔너리
def solution(price):
    discount_dict = {500000 : 0.8, 300000 : 0.9, 100000 : 0.95, 0 : 1}
    for discount_price, discount_rate in discount_dict.items():
        if price >= discount_price:
            return int(price * discount_rate)