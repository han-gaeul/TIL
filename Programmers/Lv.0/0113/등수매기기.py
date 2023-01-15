# 영어 점수와 수학 점수의 평균 점수를 기준으로
# 학생들의 등수를 매기려고 한다
# 영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때
# 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열 return

def solution(score):
    answer = []
    li = []
    for i in score:
        # score의 평균을 계산해 li 리스트에 추가
        li.append(sum(i)/len(i))
    
    # li 리스트를 내림차순으로 정렬
    array = sorted(li, reverse=True)
    for i in li:
        # 내림차순 정렬한 array에서 해당 score의 요소를 찾아
        # 1을 더한 후 answer 리스트에 추가
        answer.append(array.index(i) + 1)
    return answer