# 10101
# 삼각형의 세 각을 입력받은 다음
# 세 각의 크기가 모두 60이면 Equilateral
# 세 각의 합이 180이고 두 각이 같은 경우 Isosceles
# 세 각의 합이 180이고 같은 각이 없는 경우 Scalene
# 세 각의 합이 180이 아닌 경우 Error

# 총 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다
# 모든 정수는 0보다 크고 180보다 작다

import sys
sys.stdin = open('삼각형외우기.txt')

triangle = [int(input()) for _ in range(3)]

#* 공통조건 : 세 각의 합이 180이면
if sum(triangle) == 180:
    #* 세 각의 크기가 모두 같으면(모두 60이면)
    if triangle[0] == triangle[1] == triangle[2]:
        print('Equilateral')
    #* 세 각 중 두 개의 각이 같으면
    elif triangle[0] == triangle[1] or triangle[1] == triangle[2] or triangle[2] == triangle[0]:
        print('Isosceles')
    #* 같은 각의 크기가 없으면
    else:
        print('Scalene')
#* 세 각의 합이 180이 아니면
else:
    print('Error')