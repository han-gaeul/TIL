import sys

sys.stdin = open("2050.txt", "r")

alpha = input()

for i in alpha:
    abc = ord(i) - 64
    print(abc, end = ' ')

# 대문자 A는 유니코드 문자에 대응 되는 정수가 65
# 따라서 ord('A') - 64 를 하면 1이 됨

# 입력 받은 문자열을 for문을 사용해
# 문자열 하나하나를 읽는다.
# 입력된 문자열을 ord() 함수를 통해 정수형으로 바꾸고
# 이 값에 64를 빼면 원하는 답이 나온다.