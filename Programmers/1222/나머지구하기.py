# 중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때
# 가장 중앙에 위치하는 값을 의미
# 정수 배열 array가 매개변수로 주어질 때
# 중앙값을 return 하도록 solution 함수 완성
# array의 길이는 홀수

def solution(array):
    array = sorted(array) # 배열 정렬
    return array[len(array) // 2] # 배열의 길이를 2로 나눠 해당 배열의 중간 인덱스를 구할 수 있음
    # array[중간 인덱스] 와 같이 해당 배열에서
    # 원하는 위치에 있는 인덱스의 값 반환