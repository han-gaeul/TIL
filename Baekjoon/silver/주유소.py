# 13305

# 어떤 나라에 N개의 도시가 있다. 이 도시들은 일직선 도로 위에 있다
# 편의상 일직선을 수평 방향으로 두자. 제일 왼쪽의 도시에서 제일 오른쪽의
# 도시로 자동차를 이용하여 이동하려고 한다. 인접한 두 도시 사이의 도로들은
# 서로 길이가 다를 수 있다. 도로 길이의 단위는 km를 사용한다
# 처음 출발할 때 자동차에는 기름이 없어서 주유소에서 기름을 넣고 출발해야 한다
# 기름통의 크기는 무제한이어서 얼마든지 많은 기름을 넣을 수 있다
# 도로를 이용하여 이동할 때 1km맏 1리터의 기름을 사용한다. 각 도시에는
# 단 하나의 주유소가 있으며, 도시마다 주유소의 리터당 가격은 다를 수 있다
# 가격 단위는 원을 사용한다. 예를 들어, 이 나라에 4개의 도시가 있다고 하자
# 숫자는 그 도시에 있는 주유소의 리터당 가격이다. 도로 위에 있는 숫자는
# 도로의 길이를 표시한 것이다. 제일 왼쪽 도시에서 6리터의 기름을 넣고
# 더 이상의 주유 없이 제일 오른쪽 도시까지 이동하면 총 비용은 30원이다
# 만약 제일 왼쪽 도시에서 2리터의 기름을 넣고(2 x 5 = 10원) 다음 번 도시까지
# 이동한 후 3리터의 기름을 넣고 (3 x 2 = 6원) 다음 도시에서 1리터의 
# 기름을 넣어 (1 x 4 = 4원) 제일 오른쪽 도시로 이동하면 총 비용은 20원이다
# 또 다른 방법으로 제일 왼쪽 도시에서 2리터의 기름을 넣고(2 x 5 = 10원)
# 다음 번 도시까지 이동한 후 4리터의 기름을 넣고(4 x 2 = 8원) 제일 오른쪽
# 도시까지 이동하면 총 비용은 18원이다
# 각 도시에 있는 주유소의 기름 가격과 각 도시를 연결하는 도로의 길이를
# 입력으로 받아 제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소의
# 비용을 계산하라

# 첫번째 줄에는 도시의 개수를 나타내는 정수 N이 주어진다
# 다음 줄에는 인접한 두 도시를 연결하는 도로의 길이가 제일 왼쪽 도로부터
# N - 1개의 자연수로 주어진다
# 다음 줄에는 주유소의 리터당 가격이 제일 왼쪽 도시부터 순서대로 N개의
# 자연수로 주어진다.

# 제일 왼쪽 도시에서 제일 오른쪽 도시로 하는 최소 비용을 출력

N = int(input())
# 인접한 두 도시를 연결하는 도로의 길이 리스트
distance = list(map(int, input().split()))
# 도시별 주유소의 리터당 가격 리스트
prices = list(map(int, input().split()))
# 최소 가격 초기화
min_price = prices[0]
# 총 비용 초기화
total = 0
for i in range(N - 1):
    # 현재 위치의 가격이 이전 위치와 가격보다 싸면
    if prices[i] < min_price:
        # 최소 가격을 현재 위치의 가격으로 저장
        min_price = prices[i]
    # 현재 위치까지의 최소 가격으로 기름으로 채우고
    # 이동한 거리에 따른 비용 누적
    total += min_price * distance[i]
print(total)


# 현재 도시까지 가는데 필요한 최소 비용은 이전 도시까지 가는데
# 필요한 최소 비용에 이전 도시와 현재 도시를 잇는 도로의 길이와
# 현재 도시의 주유소 가격을 곱한 값을 더한 것과 같다
# 이전 도시와 현재 도시를 잇는 도로의 길이와 현재 도시의 주유소
# 가격을 곱한 값을 더한 것이 현재 도시까지 가는데  필요한 최소
# 비용보다 크다면, 현재 도시까지 가는데 필요한 최소 비용을 그 
# 값으로 갱신하고 현재 도시를 가장 낮은 가격의 주유소로 저장한다
# 마지막으로 현재 도시까지 가는데 필요한 최소 비용을 출력한다