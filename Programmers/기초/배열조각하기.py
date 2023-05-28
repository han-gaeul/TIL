# 정수 배열 arr와 query가 주어진다
# query를 순회하면서 다음 작업을 반복한다
# 짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고
# 배열의 query[i]번 인덱스 뒷부분을 잘라서 버린다
# 홀수 인덱스에서는 arr에서 query[i]번 인덱스는 제외하고
# 배열의 query[i]번 인덱스 앞부분을 잘라서 버린다
# 위 작업을 마친 후 남은 arr의 부분 배열을 return

def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]
    return arr