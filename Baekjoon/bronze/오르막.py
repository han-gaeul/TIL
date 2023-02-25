# 14910

# 주어진 N개의 정수가 비내림차순으로 나열되어 있는지 판정하라
# N개의 수 A1, A2, ..., An이 A1 <= A2 <= ... <= An을 만족하는 것을 비내림차순이라고 한다

# 첫째 줄에 공백으로 구분된 N개의 정수가 주어진다

# 비내림차순으로 나열되어 있으면 Good을 출력하고 그렇지 않으면 Bad를 출력



# 1.
N = list(map(int, input().split()))
sorted_N = sorted(N)
if N == sorted_N:
    print('Good')
else:
    print('Bad')
# O(n log n) 824ms
# 리스트를 정렬하는데 걸리는 시간 복잡도는 일반적으로 O(n log n)
# 여기서 n은 리스트의 크기를 나타냄
# 비교 연산은 모든 요소를 한 번씩 비교해야 하므로
# 리스트의 크기에 비례하는 O(n) 시간이 소요됨
# 따라서 이 코드의 전체 시간 복잡도는 O(n log n + n)으로
# O(n log n)에 비해 아주 근소한 작은 차이가 있다



# 2.
N = list(map(int, input().split()))
check = True
for i in range(1, len(N)):
    if N[i - 1] > N[i]:
        check = False
print('Good' if check else 'Bad')
# O(n) 524ms
# 이 코드의 시간 복잡도는 리스트 N의 크기에 비례
# 리스트 N이 오름차순으로 정렬되어 있는지 확인하는 코드는 이 코드가 최적
# 왜냐하면 어떤 두 요소를 비교할 때 하나의 요소와 그 다음 요소만 비교하면 되기 때문