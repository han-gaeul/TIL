# 점수 중에 최댓값을 고르고 이 값을 M이라고 한다
# 그리고 나서 모든 점수를 점수/M*100으로 고침

# 첫째 줄에 시험 본 과목의 개수N이 주어진다
# 둘째 줄에 현재 성적이 주어진다

# 첫째 줄에 새로운 평균을 출력
# 실제 정답과 출력값의 절대오차 또는 상대오차가 10의 -2승 이하이면 정답

N = int(input())
M = list(map(int, input().split()))
max_ = max(M)

for i in range(N):
    M[i] = M[i] / max_ * 100
print('%2f' %(sum(M) / N))