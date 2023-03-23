# H-Index는 과학자의 생산성과 영향력을 나타내는 지표이다
# 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 한다
# 위키백과에 따르면 H-Index는 다음과 같이 구한다
# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이
# h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의
# 최댓값이 이 과학자의 H-Index이다
# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가
# 매개변수로 주어질 때, 이 과학자의 H-Index를 return

def solution(citations):
    citations.sort(reverse=True)
    h = 0
    for i in range(len(citations)):
        # 논문 인용 횟수가 i + 1 이상이라면
        if citations[i] >= i + 1:
            h = i + 1
        # 논문 인용 횟수가 i + 1보다 작다면
        else:
            break
    return h



# H-Index를 구하기 위해서 주어진 논문 인용 횟수 배열을
# 내림차순으로 정렬한 후, 각 논문의 인용 횟수와 인덱스 값을
# 비교하며 H-Index를 계산한다
# 논문을 인용 횟수가 많은 순으로 정렬한 후, 인덱스 i와 정렬된
# 논문 인용 횟수 citations[i]를 비교한다. 만약 citations[i]가
# i보다 작거나 같으면, h의 값은 i이다. 이는 i번째 논문을 포함하여
# i번째 논문보다 인용 횟수가 크거나 같은 논문이 적어도 i개
# 이상이기 때문이다. 이 조건이 만족하지 않을 때까지 i를 증가시켜
# 검사를 계속한다