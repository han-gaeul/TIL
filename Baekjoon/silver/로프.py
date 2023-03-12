# 2217

# N개의 로프가 있다. 이 로프를 이용해 이런저런
# 물체를 들어올릴 수 있다
# 각각의 로프는 그 굵기나 길이가 다르기 때문에
# 들 수 있는 물체의 중량이 서로 다를 수도 있다
# 하지만 여러 개의 로프를 병렬로 연결하면 각각의
# 로프에 걸리는 중량을 나눌 수 있다.
# k개의 로프를 사용해 중량이 w인 물체를 들어올릴 때
# 각각의 로프에는 모두 고르게 w/k만큼의 중량이 걸리게 된다
# 각 로프들에 대한 정보가 주어졌을 때, 이 로프들을
# 이용해 들어올릴 수 있는 물체의 최대 중량을 구하라
# 모든 로프를 사용해야 할 필요는 없으며, 임의로 
# 몇 개의 로프를 골라서 사용해도 된다

# 첫째 줄에 정수 N이 주어진다
# 다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다

# 첫째 줄에 답을 출력

N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort(reverse=True)
# 최대 중량 초기값 설정
max_weight = 0
for i in range(N):
    # i번째로 무거운 로프까지 사용하는 경우의
    # 들어올릴 수 있는 최대 중량 계산
    weight = ropes[i] * (i + 1)
    # 현재까지 구한 최대 중량보다 크다면
    if weight > max_weight:
        # 최대 중량 업데이트
        max_weight = weight
print(max_weight)



# 입력받은 로프 중 가장 무거운 로프부터 사용하면
# 들어올릴 수 있는 최대 중량을 구할 수 있다
# 따라서, 우선 입력받은 로프들을 내림차순으로 정렬하고
# 각 로프를 사용하는 경우마다 들어올릴 수 있는
# 최대 중량을 계산한다
# 로프를 i개 사용하는 경우, i번째로 무거운 로프까지
# 사용하면서 들어올릴 수 있는 중량은 (i번째 로프의
# 버틸 수 있는 중량 * i)이다.
# 위와 같은 방법으로 계산한 중량 중에서 가장 큰 값을
# 저장하여 출력한다.