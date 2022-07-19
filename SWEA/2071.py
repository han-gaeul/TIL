
import sys

sys.stdin = open("2071.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # 띄어쓰기를 기준으로 입력된 숫자를 모두 정수 처리하고 리스트화
    numbers = list(map(int, input().split()))
    # /를 사용하여 일반 나눗셈을 한다. //로 정수 나눗셈을 하면 나눗셈을 하고 낮은 정수로 내림이 되기 때문에 사용X
    avg_value = sum(numbers) / len(numbers)
    # 일반 나눗셈을 하고 round 함수로 반올림
    avg_value = round(avg_value)
    print('#{} {}'.format(test_case, avg_value))