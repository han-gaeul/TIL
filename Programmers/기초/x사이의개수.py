# 문자열 myString이 주어진다
# myString을 문자 'x'를 기준으로 나눴을 때 나눠진 문자열 각각의
# 길이를 순서대로 저장한 배열을 return

def solution(myString):
    subStr = myString.split('x')
    lengths = [len(i) for i in subStr]
    return lengths