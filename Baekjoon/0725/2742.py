# 기찍 N
# 자연수 N이 주어졌을 때
# N부터 1까지 한 줄에 하나씩 출력

N = int(input())

for i in range(N, 0, -1):
    print(i)


# for문 이용시 range는 첫째 인자로 초기값,
# 둘째 인자로 종료값, 마지막 인자로 증가값을 적용