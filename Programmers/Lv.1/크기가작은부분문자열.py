# 숫자로 이루어진 문자열 t와 p가 주어질 때 t에서 p와 길이가 같은
# 부분문자열 중에서 이 부분문자열이 나타내는 수가 p가 나타내는 수보다
# 작거나 같은 것이 나오는 횟수를 return
# 예를 들어 t = '3141592'이고 p = '271'일 경우 t의 길이가 3인 부분문자열은
# 314, 141, 415, 159, 592이다.
# 이 문자열이 나타내는 수 중 271보다 작거나 같은 수는 141, 159 2개이다.



# 처음 생각한 코드
# 두번째 테스트 케이스 오답
def solution(t,p):
    answer = []
    for i in range(len(t)):
        word = t[i : len(p)]
        for x in word:
            if x <= p:
                answer.append(x)
    return len(answer)



# 수정한 코드
def solution(t, p):
    answer = 0
    for i in range(0, len(t) - len(p) + 1):
        if int(t[i : i + len(p)]) <= int(p):
            answer += 1
    return answer