# 문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고
# 마지막 문자는 맨 앞으로 이동시키면 "ohell"가 된다
# 이것을 문자열을 민다고 정의한다면
# 문자열 A와 B가 매개변수로 주어질 때 A를 밀어서
# B가 될 수 있다면 밀어야 하는 최소 횟수를 return
# 밀어서 B가 될 수 없으면 -1을 return

def solution(A, B):
    answer = 0
    # 문자열을 리스트화 시켜서 분리
    text = list(A)
    for i in range(len(A)):
        # 리스트로 분리한 문자열을 다시 조합해서 B와 같은지 비교
        if "".join(text) == B:
            return answer
        # 같지 않다면 text의 마지막 요소를 맨 앞으로 가져오고
        # answer에 1 추가
        else:
            text.insert(0, text.pop())
            answer += 1
    return -1


# list.insert(a, b) 리스트에 요소 삽입하기
# 리스트 a번째 위치에 b를 삽입하는 함수


solution = lambda A, B : (B * 2).find(A)

# B를 2번 반복하고 find 함수로 a의 위치를 찾으면
# 그 위치가 옮겨야 하는 횟수이다
# find()는 원하는 값을 찾지 못하면 -1을 반환