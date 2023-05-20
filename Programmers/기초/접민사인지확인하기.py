# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을
# 의미한다. 예를 들어, banana의 모든 접미사는 banana, anana,
# nana, ana, na, a이다.
# 문자열 my_string과 is_suffix가 주어질 때, is_suffix가
# my_string의 접미사라면 1을, 아니면 0을 return

def solution(my_string, is_suffix):
    ans = []
    length = len(my_string)
    for i in range(length):
        ans.append(my_string[i:])
    if is_suffix in ans:
        return 1
    else:
        return 0