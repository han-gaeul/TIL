# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행,
# 같은 열의 값을 서로 더한 결과가 된다
# 2개의 행렬 arr1과 arr2를 입력받아 행렬 덧셈의 결과를 return

def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1