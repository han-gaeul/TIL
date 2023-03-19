# Finn은 요즘 수학 공부에 빠져있다. 수학 공부를 하던 Finn은 자연수 n을
# 연속한 자연수들로 표현하는 방법이 여러개라는 사실을 알게 되었다
# 예를 들어, 15는 다음과 같이 4가지로 표현할 수 있다
# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15
# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는
# 방법의 수를 return

def solution(n):
    answer = 0
    # 시작하는 자연수
    start = 1
    # 끝나는 자연수
    end = 1
    # 현재까지 연속된 자연수들의 합
    total = 1
    while start <= n:
        # 현재까지 합이 n보다 작으면
        if total < n:
            # 끝나는 자연수 1 증가
            end += 1
            # 합에 더함
            total += end
        # 현재까지 합이 n과 같으면
        elif total == n:
            # answer 1 증가
            answer += 1
            # 합에서 시작값을 뺌
            total -=start
            # 시작값 1 증가
            start += 1
        # 현재까지 합이 n보다 크면
        else:
            # 합에서 시작값을 뺌
            total -= start
            # 시작값 1 증가
            start += 1
    return answer



n = int(input())
answer = 0
# 시작하는 자연수
start = 1
# 끝나는 자연수
end = 1
# 현재까지 연속된 자연수들의 합
total = 1
while start <= n:
    # 현재까지 합이 n보다 작으면
    if total < n:
        # 끝나는 자연수 1 증가
        end += 1
        # 합에 더함
        total += end
    # 현재까지 합이 n과 같으면
    elif total == n:
        # answer 1 증가
        answer += 1
        # 합에서 시작값을 뺌
        total -=start
        # 시작값 1 증가
        start += 1
    # 현재까지 합이 n보다 크면
    else:
        # 합에서 시작값을 뺌
        total -= start
        # 시작값 1 증가
        start += 1
print(answer)