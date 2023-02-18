# 2966

# 상근이, 창영이, 현진이는 역사와 전통을 자랑하는 Sogang ACM-ICPC Team에 가입하려고 한다
# 하지만 가입하려고 하는 모든 지원자는 C언어 필기시험을 통과해야 한다
# 이들은 C언어를 할 줄 모른다. 따라서 필기시험을 모두 찍으려고 한다
# 상근이는 A, B, C, A, B, C, A, B, C, A, B,C , ...와 같이 찍어야 통과할 수 있다고 생각한다
# 하지만 창영이는 B, A, B, C, B, A, B, C, B, A, B, C, ...와 같이 찍는 방법이 만점의 지름길이라고 생각한다
# 마지막으로 현진이는 상근이와 창영이를 비웃으면서 C, C, A, A, B, B, C, C, A, A, B, B, ...와 같이 찍어야 통과한다고 말했다
# 필기시험의 정답이 주어졌을 때 상근이, 창영이, 현진이 중에서 가장 많은 문제를 맞힌 사람이 누구인지 구하라

# 첫째 줄에 필기시험의 문제의 수 N이 주어진다
# 둘째 줄에는 시험의 정답이 주어진다

# 첫째 줄에 가장 많은 문제를 맞춘 사람이 몇 문제를 맞혔는지 출력
# 다음 줄에는 가장 많은 문제를 맞힌 사람의 아이디를 출력
# 상근이의 아이디는 Adrian, 창영이의 아이디는 Bruno,
# 현진이의 아이디는 Goran이다
# 아이디 여러 개를 출력하는 경우에는 상근이, 창영이, 현진이 순서로 출력하고
# 한 줄에 하나씩 출력


# 1.
N = int(input().strip())
answer = input().strip()
adrian = ["A","B","C"]
bruno = ["B","A","B","C"]
goran = ["C","C","A","A","B","B"]
s_score, c_score, h_score = 0, 0, 0
for i in range(N):
    if adrian[i % len(adrian)] == answer[i]:
        s_score += 1
    if bruno[i % len(bruno)] == answer[i]:
        c_score += 1
    if goran[i % len(goran)] == answer[i]:
        h_score += 1
max_score = max(s_score, c_score, h_score)
print(max_score)
if max_score == s_score:
    print("Adrian")
if max_score == c_score:
    print("Bruno")
if max_score == h_score:
    print("Goran")
# 60ms



# 2.
N = int(input().strip())
answer = input().strip()
adrian = ["A","B","C"]
bruno = ["B","A","B","C"]
goran = ["C","C","A","A","B","B"]
score = [0,0,0]
for i in range(N):
    if adrian[i % 3] == answer[i]:
        score[0] += 1
    if bruno[i % 4] == answer[i]:
        score[1] += 1
    if goran[i % 6] == answer[i]:
        score[2] += 1
max_score = max(score)
print(max_score)
if score[0] == max_score:
    print("Adrian")
if score[1] == max_score:
    print("Bruno")
if score[2] == max_score:
    print("Goran")
# 40ms
# len() 함수를 사용해서 연산하면 4ms가 늘어남