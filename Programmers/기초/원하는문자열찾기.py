# 알파벳으로 이루어진 문자열 myString과 pat이 주어진다
# myString의 연속된 부분 문자열 중 pat이 존재하면 1을,
# 그렇지 않으면 0을 return

def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    if len(myString) < len(pat):
        return 0
    for i in range(len(myString) - len(pat) + 1):
        if myString[i:i + len(pat)] == pat:
            return 1
    return 0