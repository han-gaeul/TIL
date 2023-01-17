# 한수
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면 그 수를 한수라고 함
# N이 주어졌을 때 1보다 크거나 같고
# N보다 작거나 같은 한수의 개수를 출력

N = int(input())

def hansu(N):
    count = 0
    for i in range(1, N + 1):
        num_list = list(map(int, str(i)))
        if i < 100:
            count += 1
        elif num_list[1] - num_list[0] == num_list[2] - num_list[1]:
            count += 1
    return count
print(hansu(N))


# 최종 목표는 개수를 출력하는 것. 때문에 return 값은 count가 되어야 함
# for문을 활용해 1 ~ N을 범위로 가지고 변수 i 설정
# 임의의 숫자를 저장할 num_list를 만듦
# 각각의 자리 수를 비교하기 위해서 자리수를 분리해야 함
# 때문에 먼저 문자열(str)로 전환 후 int형으로 map(전체 변환)하고 list화
# 이후 i(숫자)가 100보다 작으면 한자리 수이거나 두자리 수이므로
# 각각의 자리수를 비교할 필요 없이 무조건 한 수가 됨
# 때문에 바로 카운트를 더해준다
# 그 외의 경우 num_list(숫자를 따로 분리 시켜 놓은 것)의
# 두 번째 자리수와 첫번째 자리수의 차가
# 세번째 자리수와 두번째 자리 수의 차와 같은 경우 한수이므로 카운트를 더함