# 24060

# 오늘도 서준이는 병합 정렬 수업 조교를 하고 있다
# 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자
# N개의 서로 다른 양의 정수가 저장된 배열 A가 있다
# 병합 정렬로 배열 A를 오름차순 정렬할 경우 배열 A에 K번째 저장되는 수를 구하라

# 첫째 줄에 배열 A의 크기 N, 저장 횟수가 주어진다
# 다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., An이 주어진다

# 배열 A에 K번째 저장되는 수를 출력
# 저장 횟수가 K보다 작은면 -1 출력


import sys
input = sys.stdin.readline

def merge_sort(L):
    # 리스트의 길이가 1이면 정렬이 필요 없으므로 그대로 반환
    if len(L) == 1:
        return L
    # 리스트의 중간 인덱스 계산
    mid = (len(L)+1)//2
    # 왼쪽과 오른쪽 리스트 재귀 호출(정렬)
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    i,j = 0,0
    L2 = []
    while i < len(left) and j < len(right):
        # 왼쪽 리스트에 있는 값이 오른쪽 리스트에 있는 값보다 작으면
        if left[i] < right[j]:
            # 새로운 리스트에 왼쪽 리스트의 값 추가
            L2.append(left[i])
            # 결과 리스트에도 추가
            ans.append(left[i])
            i+=1
        else:
            # 오른쪽 리스트이 값이 작다면 새로운 리스트에 오른쪽 리스트의 값 추가
            L2.append(right[j])
            ans.append(right[j])
            j+=1
    while i < len(left):
        L2.append(left[i])
        ans.append(left[i])
        i+=1
    while j < len(right):
        L2.append(right[j])
        ans.append(right[j])
        j+=1
    return L2
n, k = map(int,input().split())
a = list(map(int,input().split()))
ans = []
merge_sort(a)
# k번째 수가 존재하다면
if len(ans) >= k:
    # k번째 출력
    print(ans[k-1])
else:
    print(-1)



# 함수 merge_sort는 입력받은 리스트 L을 인자로 받아 정렬된 리스트를 반환
# 이 함수는 재귀 호출로 구현되어 있으며 함수가 호출될 때마다 리스트를 절반으로 나눈다
# 절반으로 나눈 리스트들은 각각 재귀적으로 merg_sort 함수를 호출하여 정렬된다
# 정렬된 리스트들은 다시 하나의 리스트로 합쳐진다
# 이 과정에서 ans 리스트에는 정렬되는 과정에서 추가되는 원소들이 저장된다
# 전체 리스트가 정렬되면 K번째 원소를 ans 리스트에서 찾아 출력
# 만약 ans 리스트의 길이가 k보다 작다면 -1 출력