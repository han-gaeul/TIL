# 선분 3개가 평행하게 놓여있다. 세 선분의 시작과 끝 좌표가
# [[start, end], [start. end], [start,end]] 형태로
# 들어있는 2차원 배열 lines가 매개변수로 주어질 때
# 두 개 이상의 선분이 겹치는 부분의 길이를 return

def solution(lines):
    # 선분의 최소 길이와 최대 길이를 구함
    sets = [set(range(min(i), max(i))) for i in lines]

    # 총 3개의 선분 중 각 첫번째, 두번째가 겹치는 경우
    # 1과 3이, 2와 3이 겹치는 경우의 교집합을 구하고
    # 합집합 반환
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])