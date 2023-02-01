# 2004

# (nm)의 끝자리 0의 개수를 출력

# 첫째 줄에 정수 n, m이 들어온다

# 첫째 줄에 (nm)의 끝자리 0의 개수를 출력


n, m = map(int, input().split())
# n을 k로 나눈 횟수를 계산하는 함수
def cnt_num(n, k):
    cnt = 0
    # n이 0이 될 때까지 반복
    while n:
        # 나눈 값 추가
        n //= k
        # 나눈 횟수 추가
        cnt += n
    return cnt
# 5와 2로 나누어지는 횟수의 차이를 계산
five_cnt = cnt_num(n, 5) - cnt_num(m, 5) - cnt_num(n - m, 5)
two_cnt = cnt_num(n, 2) - cnt_num(m, 2) - cnt_num(n - m, 2)
# 두 개의 수 중에서 작은 값 출력
# 이 값은 끝자리 0의 개수가 됨
print(min(five_cnt, two_cnt))



# cnt_num 함수는 두 번째 인자인 k를 기준으로 첫 번째 인자인 n의
# 각 자릿수에 포함된 k의 개수를 계산한다
# 예를 들어 cnt_num(30, 5)는 30 // 5 + 30 // 25 + 30 // 125의 값인 6을 반환한다