# 1202

# 세계적인 도둑 상덕이는 보석점을 털기로 결심했다
# 상덕이가 털 보석점에는 보석이 총 N개가 있다
# 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 상덕이는 가방을
# K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다
# 가방에는 최대 한 개의 보석만 넣을 수 있다
# 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하라

# 첫째 줄에 N과 K가 주어진다
# 다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다
# 다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다
# 모든 숫자는 양의 정수이다

# 첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력

import heapq, sys

N, K = map(int, sys.stdin.readline().split())
jewelries = []
bags = []
# 보석들의 무게와 가격을 입력 받고 리스트에 저장
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    jewelries.append((M, V))
# 가방들의 최대 무게를 입력 받고 리스트에 저장
for _ in range(K):
    bags.append(int(sys.stdin.readline()))
# 보석을 무게 기준으로 내림차순으로 정렬
jewelries.sort(key=lambda x : -x[0])
# 힙을 이용해 최적의 보석을 선택하고, 그 가격을 더함
heap = []
res = 0
for bag in sorted(bags):
    # 현재 가방에 담을 수 있는 무게보다 작거나 같은 보석을 힙에 추가
    while jewelries and jewelries[-1][0] <= bag:
        heapq.heappush(heap, -jewelries.pop()[1])
    # 힙에 보석이 있는 경우 그 중에서 가장 가격이 높은 보석을 결과에 더함
    if heap:
        res -= heapq.heappop(heap)
print(res)



# 입력으로 주어진 보석들을 무게 기준으로 내림차순 정렬한다
# 그리고 각 가방을 무게를 기준으로 오름차순 정렬한다
# 가장 무거운 가방부터 선택하면서 해당 가방에 넣을 수 있는
# 모든 보석들을 우선순위 큐(heap)에 넣는다. 이때, 보석의 
# 가치를 기준으로 최대 힙을 사용하면 가장 가치가 높은 보석이
# 먼저 pop 되어 나오기 때문에 최대 가치를 선택할 수 있다
# 우선순위 큐에서 pop한 보석의 가치를 누적하여 결과값에
# 더하고, 다음 가방으로 넘어간다. 이때, 현재 남은 보석들 중에서
# 현재 가방에 넣을 수 있는 보석들만 우선순위 큐에 넣는다
# 이를 반복하면, 모든 가방에 대해 가장 가치가 높은 보석을
# 선택해 결과값에 누적할 수 있다.