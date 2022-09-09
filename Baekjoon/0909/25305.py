# 코딩대회에 N명의 학생들이 응시했다
# 이들 중 점수가 가장 높은 k명은 상을 받을 것이다
# 이때 상을 받는 커트라인이 몇 점인지 구하라
# 커트라인이란 상을 받는 사람들 중 점수가
# 가장 낮은 사람의 점수를 말한다

# 첫째 줄에는 응시자의 수 N과 상을 받는 사람의 수 k가 
# 공백을 사이에 두고 주어진다
# 둘째 줄에는 각 학생의 점수 x가 공백을 사이에 두고 주어진다

# 상을 받는 커트라인을 출력

N, k = map(int, input().split())
# 점수를 리스트로 입력 받음
score = list(map(int, input().split()))

# 큰 수부터 정렬
score.sort(reverse=True)
# 0으로 시작하므로 k번째 요소를 꺼내기 위해
print(score[k-1])