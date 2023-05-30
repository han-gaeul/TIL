# 문자열 리스트 str_list에는 'u', 'd', 'l', 'r' 네 개의 문자열이
# 여러개 저장되어 있다. str_list에서 'l'과 'r' 중 먼저 나오는
# 문자열이 'ㅣ'이라면 해당 문자열을 기준으로 왼쪽에 있는
# 문자열들을 순서대로 담은 리스트를, 먼저 나오는 문자열이
# 'r' 이라면 해당 문자열을 기준으로 오른쪽에 있는 문자열들을
# 순서대로 담은 리스트를 return
# 'l'이나 'r'이 없다면 빈 리스트를 return

def solution(str_list):
    l_index = float('inf')
    r_index = float('inf')
    for i in range(len(str_list)):
        if str_list[i] == "l":
            l_index = i
            break
        elif str_list[i] == "r":
            r_index = i
            break
    if l_index == float('inf') and r_index == float('inf'):
        return []
    if l_index < r_index:
        return str_list[:l_index]
    elif r_index < l_index:
        return str_list[r_index+1:]
    else:
        return []