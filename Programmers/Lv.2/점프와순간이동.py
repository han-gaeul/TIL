# OO 연구소는 한 번에 K칸을 앞으로 점프하거나,
# (현재까지 온 거리) x 2에 해당하는 위치로 순간이동을 할 수 있는
# 특수한 기능을 가진 아이언 슈트를 개발해 판매하고 있다
# 이 아이언 슈트는 건전지로 작동되는데, 순간이동을 하면 건전지
# 사용량이 줄지 않지만, 앞으로 K칸을 점프하면 K만큼의 건전지
# 사용량이 든다. 그러므로 아이언 슈트를 착용하고 이동할 때는
# 순간 이동을 하는 것이 더 효율적이다. 아이언 슈트 구매자는
# 아이어 슈트를 착용하고 거리가 N만큼 떨어져 있는 장소로 가려고 한다.
# 단, 건전지 사용량을 줄이기 위해 점프로 이동하는 것은 최솔 하려고 한다
# 아이어 슈트 구매자가 이동하려는 거리 N이 주어졌을 때
# 사용해야 하는 건전지 사용량의 최솟값을 return
# 예를 들어, 거리가 5만큼 떨어져 있는 장소로 가려고 한다
# 아이언 슈트를 입고 거리가 5만큼 떨어져 있는 장소로 갈 수 있는
# 경우의 수는 여러 가지이다.

def solution(N):
    # 건전지 사용량을 저장할 변수
    answer = 0
    while N > 0:
        # N이 2의 배수라면 순간이동 가능
        if N % 2 == 0:
            N //= 2
        # N이 2의 배수가 아니라면 점프를 해야 함
        else:
            # 이동거리 감소
            N -= 1
            # 건전지 사용량 증가
            answer += 1
    return answer



# 이 문제에서 핵심은 '순간이동의 비용이 크지 않다.'는 것이다
# 순간이동의 비용이 크기 않기 때문에 이진 탐색을 이용해
# 최적의 해를 구할 수 있다
# 먼저, 거리 N을 이동할 때 필요한 최소 건전지 사용량의 최댓값을
# 구한다. 최소 건전지 사용량의 최댓값은 아이언 슈트를 입지 않았을
# 때의 이동 방법으로 구할 수 있다. 예를 들어, 거리 N이 7일 때
# 최소 건전지 사용량의 최댓값은 3이다.
# 최소 건전지 사용량을 구한 후 이진 탐색을 진행한다. 이진 탐색을
# 진행할 때, mid값을 구해 mid번 순간이동을 했을 때 거리를 이동할 수
# 있는지 확인한다. 이동할 수 있다면, mid + 1번에서 시작하는 이진
# 탐색을 진행한다. 이동할 수 없다면, mid - 1에서 시작하는 이진 탐색을
# 진행한다. 최종적으로 이동할 수 있는 mid값이 정답이 된다.
