# 정수 배열 array와 정수 n이 매개변수로 주어질 때
# array에 들어있는 정수 중 n과 가장 가까운 수를 return

def solution(array, n):
    box = []
    array.sort()
    for i in array:
        box.append(abs(n - i))
    answer = [array[box.index(min(box))]]
    if len(answer) > 1:
        return min(answer)
    else:
        return answer[0]


solution = lambda a, n : sorted(a, key=lambda x : (abs(x - n), x))[0]