# 문자열 myString이 주어진다
# x를 기준으로 해당 문자열을 잘라내 배열을 만든 후 사전순으로
# 정렬한 배열을 return

def solution(myString):
    subStr = myString.split('x')
    subStr = [i for i in subStr if i]
    return sorted(subStr)