import sys

sys.stdin = open("1288.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # 값을 담을 result
    result = set()
    count = 1
    while True:
        # 리스트에 있는 값을 number로 하나씩 넣고
        for number in list(str(N)):
            # reuslt에 number 추가
            result.add(number)
        # reulst의 길이가 10이면 break  
        if len(result) == 10:
            break
        # N을 1로 만들기 위해 count로 나눠서 몫을 할당 함
        N //= count
        count += 1
        N *= count
    print('#{} {}'.format(test_case, N))

# 중복이 허용되지 않는 세트의 특징을 활용해
# 매번 세트의 길이를 세는 방식