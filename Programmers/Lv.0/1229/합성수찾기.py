# 약수의 개수가 세 개 이상인 수를 합성수라고 한다.
# 자연수 n이 매개변수로 주어질때 n 이하의 합성수의 개수를 return

def solution(n):
    num = []
    cnt = 0
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                num.append(i)
        if num.count(i) >= 3:
            cnt += 1
    return cnt