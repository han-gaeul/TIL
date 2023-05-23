# 알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때
# my_string에서 'A'의 개수, my_string에서 'B'의 개수, ...,
# my_string에서 'Z'의 개수, my_string에서 'a'의 개수,
# my_string에서 'b'의 개수, ..., my_string에서 'z'의 개수를
# 순서대로 담은 길이 52의 정수 배열을 return

def solution(my_string):
    cnt = [0] * 52
    for char in my_string:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
        elif 'a' <= char <= 'z':
            index = ord(char) - ord('a') + 26
        else:
            continue
        cnt[index] += 1
    return cnt