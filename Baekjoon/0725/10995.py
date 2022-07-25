# 별 찍기 20
# 예제를 보고 규칙을 유추한 뒤 출력

# 입력 : 1
# 출력 : *
# 입력 : 2
# 출력
# **
#  **
# 입력 : 3
# 출력
# ***
#  ***
# ***

star_num = int(input())

if star_num == 1:
    print('*')
else:
    for star in range(star_num):
        if star % 2 == 0:
            print('* ' * star_num)
        else:
            print(' *' * star_num)