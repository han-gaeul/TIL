# 2661

# 숫자 1, 2, 3으로만 이루어지는 수열이 있다
# 임의의 길이의 인접한 두 개의 부분 수열이 동일한 것이 있으면
# 그 수열을 나쁜 수열이라고 부른다
# 그렇지 않은 수열은 좋은 수열이다
# 다음은 나쁜 수열의 예이다
# 33, 32121323, 123123213
# 다음은 좋은 수열의 예이다
# 2, 32, 32123, 1232123
# 길이가 N인 좋은 수열들을 N자리의 정수로 보아 그중 가장 작은 수를
# 나타내는 수열을 구하라
# 예를 들면 1213121과 2123212는 모두 좋은 수열이지만
# 그 중에서 작은 수를 나타내는 수열은 1213121이다

# 입력은 숫자 N하나로 이루어진다

# 첫번쨰 줄에 1, 2,3으로만 이루어져 있는 길이가 N인 좋은 수열들 중에서
# 가장 작은 수를 나타내는 수열만 출력
# 수열을 이루는 1, 2, 3들 사이에는 빈칸을 두지 않는다

# 선택한 숫자와 자릿수를 입력받 이전에 선택한 숫자와
# 뒤에서부터 일정 범위만큼 같은지 확인하는 함수 정의
def choose(res, cnt):
    # 이전에 선택한 숫자와 뒤에서부터 일정 범위만큼 같으면 중복되므로 return
    for i in range(1, cnt // 2 + 1):
        if str(res)[cnt - i:] == str(res)[cnt - 2 * i:cnt - i]:
            return
    # 자릿수가 N이면 최종 결과값을 출력하고 종료
    if cnt == N:
        print(res)
        exit()
    # 자릿수가 N이 아니면 1부터 3까지의 수 중 하나를 선택하여
    # 선택한 숫자에 추가하고 자릿수를 1 증가시켜 재귀 호출
    for i in range(1, 4):
        t = res * 10 + i
        choose(t, cnt + 1)
# 자릿수를 입력받아 choose 함수에 0, 0을 전달하여 호출
N = int(input())
choose(0, 0)


# 이 문제에서는 백트래킹을 사용해 숫자를 생성하는 과정에서
# 중복되는 수열을 만들어내지 않도록 한다
# 백트래킹은 가능한 모든 경우를 탐색하여 문제를 해결하는 알고리즘이다
# choose 함수는 현재 선택한 숫자와 그 숫자의 자릿수를 입력으로 받는다
# 이전에 선택한 숫자와 뒤에서부터 일정 범위만큼 같은지 확인하여
# 중복되는 수열을 만들어내지 않도록 한다
# 자릿수가 N이 아니면 1부터 3까지의 수 중 하나를 선택한 숫자에 추가하고
# 자릿수를 1 증가시켜서 재귀 호출한다. 이 과정에서 중복되는 수열이
# 만들어지지 않도록 choose 함수 내에서 미리 검사하기 때문에
# 중복되는 수열이 만들어지지 않는다