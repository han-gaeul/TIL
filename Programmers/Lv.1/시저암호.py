# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는
# 암호화 방식을 시저 암호라고 한다
# 예를 들어 'AB'는 1만큼 밀면 'BC'가 되고 3만큼 밀면 'DE'가 된다
# 'z'는 1만큼 밀면 'a'가 된다
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 return

def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    return ''.join(s)


# ord(s[i]) - ord('a')으로 s[i]의 아스키 코드 값을 구한 뒤 'a'의 아스키 코드 값을 뺀다
# 그리고 이동시킬 n만큼의 숫자를 더한다
# 알파벳이 25글자이므로 26로 나머지 연산자를 이용해서
# z처럼 마지막이 다시 처음으로 돌아갈 수 있게 하고
# 또 'a'의 아스키 코드를 더하면 원하는 소문자의 아스키 코드 값을 받을 수 있다
