# 정수 배열 arr가 주어진다. arr의 각 원소에 대해 값이 50보다
# 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를
# 곱하고 다시 1을 더한다
# 이러한 작업을 x번 반복한 결과인 배열을 arr(x)라고 표현했을 때
# arr(x) = arr(x + 1)인 x가 항상 존재한다. 이러한 x 중 가장
# 작은 값을 return
# 단, 두 배열에 대한 '='는 두 배열의 크기가 서로 같으며
# 같은 인덱스의 원소가 각각 서로 같음을 의미한다.

def solution(arr):
    x = 0
    while True:
        new_arr = arr[:]
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                new_arr[i] = arr[i] // 2
            elif arr[i] < 50 and arr[i] % 2 != 0:
                new_arr[i] = arr[i] * 2 + 1
        x += 1
        if new_arr == arr:
            break
        arr = new_arr
    return x - 1