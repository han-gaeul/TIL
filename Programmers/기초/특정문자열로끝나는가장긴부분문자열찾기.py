# 문자열 myString과 pat가 주어진다
# myString의 부분 문자열 중 pat로 끝나는 가장 긴 부분 문자열을
# 찾아서 return

def solution(myString, pat):
    res = []
    for i in range(len(myString)):
        curStr = myString[:i + 1]
        if curStr.endswith(pat):
            res.append(curStr)
    res.sort(key=lambda x : len(x), reverse=True)
    return res[0] if res else myString