# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는
# 문자열을 의미한다. 예를 들어 'banana'의 모든 접미사는
# 'banana', 'anana', 'nana', 'na', 'a'이다
# 문자열 my_string이 매개변수로 주어질 때 my_string의 
# 모든 접미사를 사전순으로 정렬한 문자열 배열을 return

def solution(my_string):
    ans = []
    length = len(my_string)
    for i in range(length):
        ans.append(my_string[i:])
    return sorted(ans)