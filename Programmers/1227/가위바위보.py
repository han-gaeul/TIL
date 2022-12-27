# 가위는 2, 바위는 0, 보는 5로 표현한다
# 가위바위보를 내는 순서대로 나타낸 문자열 rsp가
# 매개변수로 주어질 때 rsp에 저장된 가위바위보를
# 모두 이기는 경우를 순서대로 나타낸 문자열을 return

def solution(rsp):
    dict = {'2' : '0', '0' : '5', '5' : '2'}
    return ''.join(map(str, [dict[x] for x in rsp]))