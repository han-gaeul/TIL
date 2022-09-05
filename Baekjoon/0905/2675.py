# 문자열 S를 입력받은 후에 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력
# 첫 번째 문자를 R번 반복하고 두 번째 문자를 R번 반복하는 식으로 P를 만듦
# S에는 QR code 'alphanumeric' 문자만 들어있다
# QR Code "alphanumeric" 문자는
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다
# 각 테스트 케이스는 반복 횟수 R, 문자열 S가 공백으로 구분되어 주어진다

# 각 테스트 케이스에 대해 P를 출력

T = int(input())

for i in range(T):
    num, S = input().split()
    text = ''

    # num(반복 횟수)와 문자열을 곱함
    for i in S:
        text += int(num) * i
    print(text)