# 문자열 S가 주어졌을 때 S의 서로 다른 부분 문자열의 개수 구하기
# 부분 문자열은 S에서 연속된 일부분을 말한다
# 예) ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc,
# aba, bab, abc, abab, babc, ababc가 있고
# 서로 다른 것의 개수는 12개다

# 첫째 줄에 문자열 S가 주어진다
# S는 알파벳 소문자로만 이루어져있다

# 첫째 줄에 S의 서로 다른 부분 문자열의 개수를 출력

S = input()
# 부분 문자열을 받을 집합 ans 선언
ans = set()

# 이중 for문을 돌면서 부분 문자열 temp를 구하고
# temp를 ans에 추가
# ans가 집합이기 때문에 중복된 문자열을 추가하지 않음
for i in range(len(S)):
    for j in range(i, len(S)):
        temp = S[i : j + 1]
        ans.add(temp)

# ans의 길이 출력
print(len(ans))