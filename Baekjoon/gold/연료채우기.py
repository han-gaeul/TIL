# 1826

# 성경이는 트럭을 정글 속에서 운전하다가 트럭의 연료탱크에 갑자기 구멍이 나서
# 1km를 가는데 1L의 연료가 새 나가게 되었다. 이것을 고치기 위해서는 가장 가까운
# 마을에 가야 한다. 그런데 그냥 가다가는 중간에 연료가 다 빠질 수 있다.
# 다행스럽게도 정글 곳곳에 연료를 채울 수 있는 주유소가 N개 있다. 그런데 정글
# 속에서 중간에 차를 멈추는 행위는 매우 위험한 행위이므로 주유소에서 멈추는
# 횟수를 최소화하려 한다. 그리고 다행히도 성경이의 트럭은 매우 좋아서 연료 
# 탱크에는 연료의 제한이 없어 많이 충분히 많이 넣을 수 있다고 한다. 각각의 주유소의
# 위치와, 각 주유소에서 얻을 수 있는 연료의 양이 주어져 있을 때, 주유소에서
# 멈추는 횟수를 구하라
# 정글은 일직선이고 성경이의 트럭과 주유소도 모두 일직선 위에 있다
# 주유소는 모두 성경이의 트럭을 기준으로 오른쪽에 있다

# 첫째 줄에 주유소의 개수 N이 주어지고 두번째 줄부터 N + 1번째 줄까지
# 주유소의 정보가 주어진다
# 주유소의 정보는 두 개의 정수 a, b로 이루어져 있는데 a는 성경이의 시작위치에서
# 주유소까지의 거리, 그리고 b는 그 주유소에서 채울 수 있는 연료의 양을 의미한다
# 그리고 N + 2번째 줄에는 두 정수 L과 P가 주어지는데 L은 성경이의 위치에서
# 마을까지의 거리, P는 트럭에 원래 있던 연료의 양을 의미한다
# 모든 주유소와 마을은 서로 다른 좌표에 있고 마을은 모든 주유소보다 오른쪽에 있다

# 첫째 줄에 주유소에서 멈추는 횟수를 출력
# 만약 마을에 도착하지 못할 경우 -1 출력

import heapq

N = int(input())
# 주유소의 정보를 저장할 리스트
stations = []
for _ in range(N):
    distance, fuel = map(int, input().split())
    # (거리, 연료) 튜플을 리스트에 추가
    stations.append((distance, fuel))
L, P = map(int, input().split())
# 거리를 기준으로 주유소를 오름차순 정렬
stations.sort()
# 연료를 저장할 우선순위 큐
pq = []
# 주유소에서 멈추는 횟수
ans = 0
# 현재 위치
pos = 0
# 현재 연료 양
tank = P
for i in range(N):
    # 다음 주유소까지의 거리
    dist = stations[i][0] - pos
    # 현재 연료로 다음 주유소에 도달할 수 없는 경우
    while tank - dist < 0:
        # 연료를 보충할 주유소가 없다면
        if not pq:
            print(-1)
            exit()
        # 연료 우선순위 큐에서 연료를 꺼내 보충
        tank += -heapq.heappop(pq)
        ans += 1
    # 다음 주유소까지의 거리만큼 연료 소비
    tank -= dist
    # 현재 위치를 다음 주유소의 위치로 업데이트
    pos = stations[i][0]
    # 현재 주유소에서 얻을 수 있는 연료를 우선순위 큐에 추가
    heapq.heappush(pq, -stations[i][1])
# 마을까지 도달할 수 없는 경우
while tank - (L - pos) < 0:
    # 연료를 보충할 주유소가 없다면
    if not pq:
        print(-1)
        exit()
    # 연료 우선순위 큐에서 연료를 꺼내 보충
    tank += -heapq.heappop(pq)
    ans += 1
print(ans)



# stations 리스트를 거리 기준으로 오름차순 정렬한다
# 현재 위치에서부터 갈 수 있는 최대 거리를 계산하고, 현재 연료량이
# dist보다 작으면, pq에서 가장 큰 주유 가능 연료량을 가진 주유소를
# 선택한다. 선택한 주유소의 연료를 tank에 추가하고, 방문한 주유소의
# 수를 1 증가한다. 위 과정을 반복하면서 현재 위치를 갱신한다
# 도착지점까지 갈 수 있는 연료가 충분하지 않으면, pq에서 가장 큰
# 주유 가능 연료량을 가진 주유소를 선택한다. 선택한 주유소의 연료를
# tank에 추가하고, 방문한 주유소의 수를 1 증가한다.
# 마지막으로 주유소를 방문한 횟수를 출력한다

# 이 코드에서는 우선순위 큐(pq)를 사용한다. pq는 현재까지 선택하지
# 않은 주유소 중에서 가장 주유 가능한 연료량을 저장하는데, 이때 주유
# 가능한 연료량을 음수로 저장하고, 가장 큰 값을 가진 주유소가 가장
# 우선 순위가 높게 한다. 이렇게 하면 pq에서 가장 큰 값을 가진 주유소가
# 우선적으로 선택되어, 현재 위치에서 갈 수 있는 최대 거리보다 연료가
# 부족한 경우 이 주유소를 선택한다.
# 또한, pq에서 주유소를 선택한 이후에는 선택한 주유소의 연료를 tank에
# 추가하고, 방문한 주유소의 수를 1 증가시켜야 한다. 이를 통해 현재 위치에서
# 다음 주유소까지 갈 수 있는 최대 거리와 현재 연료량을 갱신하고
# 이를 반복해 도착지점까지 갈 수 있는 최소한의 주유소 방문 횟수를 구할 수 있다