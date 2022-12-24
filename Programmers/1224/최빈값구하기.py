# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미
# 정수 배열 array가 매개변수로 주어질 때
# 최빈값을 return 하도록 solution 함수 완성
# 최빈값이 여러개면 -1을 return 

# 1. 리스트
def solution(array):
    # [빈도, 숫자]
    times_list = [[0, i] for i in range(max(array) + 1)]
    for num in array:
        times_list[num][0] += 1
    times_list.sort(reverse=True)
    return times_list[0][1] if times_list[0][0] != times_list[1][0] else -1

# 2. 딕셔너리
def solution(array):
    times_dict = {}
    for num in array:
        # setdefault(key[, default])
        # key가 딕셔너리에 있으면 해당 값을 돌려줌
        # 그렇지 않으면 default 값을 갖는 key를 삽입 후 default를 돌려줌
        # default의 기본값은 None
        times_dict.setdefault(num, 0)
        times_dict[num] += 1
    # lambda 매개변수 : 표현식
    times_list = sorted(times_dict.items(), key=lambda x : x[1], reverse=True)
    if len(times_list) > 1:
        return times_list[0][0] if times_list[0][1] != times_list[1][1] else -1
    return times_list[0][0]

# 3. Counter
# 중복된 데이터가 저장된 배열을 인자로 넘기면
# 각 원소가 몇 번씩 나오는지 저장된 객체를 얻게 됨
from collections import Counter

def solution(array):
    # Counter(x).most_common(n)
    # x의 요소를 세어 최빈값 n개를
    # 리스트에 담긴 튜플 형태로 반환
    counter = Counter(array).most_common()
    if len(counter) > 1:
        return -1 if counter[0][1] == counter[1][1] else counter[0][0]
    return counter[0][0]