# 숫자 카드 N장을 가지고 있다
# 숫자 카드에는 정수가 하나 적혀있는데
# 적혀있는 수는 -2의 62승보다 크거나 같고 2의 62승보다 작거나 같다
# 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하라
# 만약 가장 많이 가지고 있는 정수가 여러 가지라면 작은 것 출력

# 첫째 줄에 준규가 가지고 있는 숫자 카드의 개수 N이 주어진다
# 둘째 줄부터 N개 줄에는 숫자 카드에 적혀있는 정수가 주어진다

# 첫째 줄에 가장 많이 가지고 있는 정수 출력

n = int(input())
numbers = {}

for _ in range(n):
    num = int(input())
    
    if num in numbers:
        numbers[num] += 1
    else:
        numbers[num] = 1

result = sorted(numbers.items(), key = lambda x : (-x[1], x[0]))
print(result[0][0])

# 카드 번호를 key로 저장하고
# 해당 카드가 들어올 때마다 value값을 1씩 증가시켜 카드의 개수를 저장
# 딕셔너리를 사용한 이유는 key값에 카드의 번호를 저장하고
# value값에 카드의 개수를 저장하여 마지막에 value값을
# 내림차순 하고, 같다면 key값을 오름차순하기 위함