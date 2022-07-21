import sys

sys.stdin = open("1989.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    word = input()
    # word의 길이 // 2를 해서 몫 값을 i에 하나씩 넣고
    for i in range(len(word) // 2):
        # word의 인덱스를 비교
        # word[i]는 0, 1, 2, ... 방향으로 진행
        # word[-1 -i]는 -1, -2, -3, ... 방향으로 진행
        # i 는 인덱스 위치
        if word[i] == word[-1 -i]:
            answer = 1
        else:
            answer = 0
    print('#{} {}'.format(test_case, answer))