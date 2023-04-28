# 문자열 code가 주어진다
# code를 앞에서부터 읽으면서 만약 문자가 1이면 mode를 바꾼다
# mode에 따라 code를 읽어가면서 문자열 ret를 만들어낸다
# modesms 0과 1이 있으며 idx를 0부터 code의 길이 - 1까지
# 1씩 키워나가면서 code[idx]의 값에 따라 다음과 같이 행동한다
# mode가 0일 때 code[idx]가 1이 아니면 idx가 짝수일 때만
# ret의 code[idx]를 추가한다
# code[idx]가 1이면 mode를 0에서 1로 바꾼다
# mode가 1일 때 code[idx]가 1이 아니면 idx가 홀수일 때만
# ret의 맨 뒤에 code[idx]를 추가한다
# code[idx]가 1이면 mode를 1에서 0으로 바꾼다
# 문자열 code를 통해 만들어진 문자열 ret를 반환
# 단, 시작할 때 mode는 0이며 반환하려는 ret이 만약
# 빈 문자열이라면 대신 EMPTY를 반환

def solution(code):
    ret = ''
    mode = 0
    for idx in range(len(code)):
        if code[idx] == '1':
            mode = 1 - mode # 모드 변경
        elif mode == 0:
            if idx % 2 == 0:
                ret += code[idx]
        else:
            if idx % 2 == 1:
                ret += code[idx]
    if ret == '':
        return 'EMPTY'
    return ret