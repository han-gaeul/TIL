# 9094

# 두 정수 n과 m이 주어졌을 때 0 < a < b < n인 정수 쌍 (a, b) 중에서
# (a제곱 + b제곱 + m) / (ab)가 정수인 쌍의 개수를 구하라

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다
# 각 테스트 케이스는 한 줄로 이루어져 있으며 n과 m이 주어진다

# 각 테스트 케이스마다 문제의 조건을 만족하는 (a, b) 쌍의 개수를 출력

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    cnt = 0
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if (a ** 2 + b ** 2 + m) % (a * b) == 0:
                cnt += 1
    print(cnt)



# 주어진 범위 내에서 a와 b를 선택하여
# 특정 조건을 만족하는 경우를 카운팅하는 방식으로 문제를 해결