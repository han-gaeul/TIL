# 머쓱이네 양꼬치 가게는 10인분을 먹으면
# 음료수 하나를 서비스로 준다.
# 양꼬치는 1인분에 12,000원
# 음료수는 2,000원이다.
# 정수 n과 k가 매개변수로 주어졌을 때
# 양꼬치 n인분과 음료수 k개를 먹었다면
# 총 얼마를 지불해야 하는지 return

def solution(n, k):
    food = n * 12000
    if n >= 10:
        drink = (k - n // 10) * 2000
    else:
        drink = k * 2000
    answer = food + drink
    return answer