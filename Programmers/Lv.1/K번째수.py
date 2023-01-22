# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때
# k번째에 있는 수를 구한다
# 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3 이라면
# 1. array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]이다
# 2. 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]이다
# 3. 2에서 나온 배여의 3번째 숫자는 5이다
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가
# 매개변수로 주어질 때 commands의 모든 원소에 대해
# 앞서 설명한 연산을 적용했을 때 나온 결과를
# 배열에 담아 return

def solution(array, commands):
    return list(map(lambda x : sorted(array[x[0] -1 : x[1]]) [x[2] - 1], commands))