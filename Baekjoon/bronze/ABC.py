# 3047

# 세 수 A, B, C가 주어진다
# A는 B보다 작고 B는 C보다 작다
# 세 수 A, B, C가 주어졌을 때 입력에서 주어진 순서대로 출력

# 첫째 줄에 세 수 A, B, C가 주어진다
# 하지만 순서는 A, B, C가 아닐 수도 있다
# 둘째 줄에는 A, B, C로 이루어진 세 글자가 주어지며
# 이 순서대로 출력

# 주어진 세 수를 주어진 출력 순서대로 출력


# 1.
arr = list(map(int, input().split()))
arr.sort()
sequence = input()
dict_ = {'A' : 0, 'B' : 1, 'C' : 2}
# arr 리스트에서 dict_에 저장된 각 알파벳의 인덱스에 해당하는 값 출력
print(arr[dict_[sequence[0]]], arr[dict_[sequence[1]]], arr[dict_[sequence[2]]])


# 2.
arr = list(map(int, input().split()))
arr.sort()
sequence = list(input())
for i in sequence:
    if i == 'A':
        print(arr[0], end=' ')
    elif i == 'B':
        print(arr[1], end=' ')
    elif i == 'C':
        print(arr[2], end=' ')
# 입력값에 대한 직접적인 처리를 하기 때문에
# 코드가 더 길어질 수 있지만 입력값이 복잡한 경우 대처가 유연함