# 1부터 6까지 숫자가 적힌 주사위가 세개 있다
# 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때
# 얻는 점수는 다음과 같다
# 세 숫자가 모두 다르다면 a + b + c점을 얻는다
# 세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면
# (a + b + c) x (a제곱 + b제곱 + c제곱)점을 얻는다
# 세 숫자가 모두 같다면 (a + b + c) x (a제곱 + b제곱 + c제곱)
# x (a세제곱 + b세제곱 + c세제곱)점을 얻는다
# 세 정수 a, b, c가 매개변수로 주어질 때 얻는 점수를 반환

def solution(a, b, c):
    if a != b and b != c and a != c:
        return a + b + c
    elif a == b == c:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    else:
        nums = [a, b, c]
        for num in set(nums):
            if nums.count(num) == 2:
                return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)