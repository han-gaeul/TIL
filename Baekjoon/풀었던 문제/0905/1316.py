# 그룹 단어란 단어에 존재하는 모든 문자에 대해서
# 각 문자가 연속해서 나타나는 경우만을 말한다
# 예를 들면 ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다
# 단어 N개를 입력 받아 그룹 단어의 개수를 출력

# 첫째 줄에 단어의 개수 N이 들어온다
# 둘째 줄부터 N개의 줄에 단어가 들어온다

# 첫째 주에 그룹 단어의 개수를 출력

N = int(input())
# 입력 받을 단어의 개수만큼 count에 저장
count = N

for i in range(N):
    word = input()

    for j in range(0, len(word)-1):
        # word[j]가 word[j + 1]과 같으면 패스
        if word[j] == word[j + 1]:
            pass
        # word[j]가 word에 포함 되어 있으면
        elif word[j] in word[j + 1:]:
            # count에서 1씩 빼기
            count -= 1
            break

print(count)