# 효진이는 멀리 뛰기를 연습하고 있다. 효진이는 한 번에 1칸,
# 또는 2칸을 뛸 수 있다. 칸이 총 4개 있을 때 효진이는
# (1칸, 1칸, 1칸, 1칸)
# (1칸, 2칸, 1칸)
# (1칸, 1칸, 2칸)
# (2칸, 1칸, 1칸)
# (2칸, 2칸)
# 의 5가지 방법으로 맨 끝 칸에 도달할 수 있다. 멀리뛰기에 사용될
# 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지
# 알아내, 여기에 1234567을 나눈 나머지를 return
# 예를 들어 4가 입력된다면 5를 return

def solution(n):
    dp = [0, 1, 2]
    for i in range(3, n + 1):
        dp.append((dp[i - 1] + dp[i - 2]) % 1234567)
    return dp[n]



# 이 문제에서는 1칸 혹은 2칸씩 이동하는 방법으로 마지막 칸까지
# 도달하는 방법의 개수를 구해야 한다. 이때, 처음 시작점에서 한 칸만
# 이동하면 1개, 두 칸 이동하면 2개의 경우가 가능하다. 이를 기반으로
# i번째 칸까지 도달하는 방법의 수를 dp[i]로 정의한다
# 그리고나서, i번째 칸으로 도달하는 방법은 i - 1번째 칸에서 한 칸을
# 이동하거나, i - 2번째 칸에서 두 칸을 이동하는 것이다
# 이때, i - 1번째 칸으로부터 도달할 수 있는 방법의 수는 dp[i - 1]이고,
# i - 2번째 칸으로부터 도달할 수 있는 방법의 수는 dp[i - 2]이다
# 그렇기 때문에 dp[i] = dp[i - 1] + dp[i - 2]로 구할 수 있다
# 하지만, i = 1일 때 dp[0]은 이전 칸이 없기 때문에 경우의 수가 0개이며
# i = 2일 때는 dp[2]가 2이기 때문에 초기값을 [0, 1, 2]로 설정해야 한다