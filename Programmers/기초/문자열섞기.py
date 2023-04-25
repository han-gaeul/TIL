# 길이가 같은 두 문자열 str1과 str2가 주어진다
# 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서
# 한 번씩 등장하는 문자열을 만들어 반환

def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    return answer