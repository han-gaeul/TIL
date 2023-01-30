# 4153

# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각삼각형인 것을 알아냈다
# 주어진 세 변의 길이로 삼각형이 직각인지 아닌지 구분하라

# 입력은 여러개의 테스트케이스로 주어지며 마지막 줄에는 0 0 0이 입력된다

# 각 입력에 대해 직각삼각형이 맞다면 'right', 아니라면 'wrong'을 출력

while True:
    triangle = list(map(int, input().split()))
    if triangle[0] == 0 and triangle[1] == 0 and triangle[2] == 0:
        break
    triangle.sort()
    if triangle[2] ** 2 == triangle[0] ** 2 + triangle[1] ** 2:
        print('right')
    else:
        print('wrong')


# 피타고라스의 정리
# 직각삼각형에서 빗변의 길이의 제곱은 다른 두 변의 길이의 제곱의 합과 같다
# 피타고라스 정리의 역
# 세 변의 길이가 a, b, c인 삼각형에서 a ** 2 + b ** 2 = c ** 2이면
# c가 빗변인 직각삼각형이다