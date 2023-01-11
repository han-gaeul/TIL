# 3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에
# 3의 배수와 숫자 3을 사용하지 않는다
# 3x 마을 사람들의 숫자는 다음과 같다
# 10진법 3x마을에서쓰는숫자
# 1 1
# 2 2
# 3 4
# 4 5
# 5 7
# 6 8
# 7 10
# 8 11
# 9 14
# 10 16
# 정수 n이 매개변수로 주어질 때 n을 3x 마을에서
# 사용하는 숫자로 바꿔 return

def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer

# 명시된 표의 규칙
# 3을 포함하거나 3의 배수인 숫자인 경우 1을 더해야함