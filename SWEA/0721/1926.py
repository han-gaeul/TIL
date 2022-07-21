import sys

sys.stdin = open("1926.txt", "r")


number = int(input())
# 출력하지 않을 숫자를 리스트로 만들기
clap = ['3', '6','9']

for i in range(1, number + 1):
    count = 0
    # 문자열로 변환한 i를 j에 하나씩 넣고
    for j in str(i):
        # j가 clap 안에 있다면
        if j in clap:
            # count에 1을 더함
            count += 1
    # count가 0보다 크다면
    if count > 0:
        # count의 숫자만큼 - 를 곱해서 i에 할당
        # count가 2라면 -가 2번 출력 됨
        i = '-' * count
    print(i, end = ' ')