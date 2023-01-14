# 프로그래머스 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급한다
# 쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고
# 서비스 치킨에도 쿠폰이 발급된다.
# 시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때
# 받을 수 있는 최대 서비스 치킨의 수를 return

def solution(chicken):
    answer = 0
    while chicken >= 10:
        # chicken을 10으로 나눈 몫과 나머지를 한번에 저장
        div, mod = divmod(chicken, 10)
        answer += div
        chicken = div + mod
    return answer


# divmod()
# 매개변수로 두 개의 숫자를 입력받아 몫과 나머지를 튜플로 반환
# 큰 숫자를 다룰 때 효율적임