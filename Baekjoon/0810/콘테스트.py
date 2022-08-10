# 5576
# W 대학과 K 대학의 컴퓨터 클럽은 이전부터 라이벌 관계에 있어
# 이 콘테스트를 이용하여 양자의 우열을 정하자라는 것
# 두 다핵에서 모두 10명씩 콘테스트에 참여
# 참가한 10명 중 득점이 높은 사람에서 3명의 점수를 합산하여
# 대학의 득점으로 하기로 했다

# 입력은 20행으로 구성된다
# 1번째 줄부터 10번째 줄에는 W 대학의 각 참가자의 점수를
# 11번째 줄부터 20번째 줄에는 K 대학의 각 참가자의 점수를 입력

# W 대학 점수와 K 대학의 점수를 순서대로 공백으로 구분하여 출력

import sys
sys.stdin = open('콘테스트.txt')

#* 점수 입력 받기
WUniversity = [int(input()) for _ in range(10)]
KUniversity = [int(input()) for _ in range(10)]

#* 높은 점수부터 정렬
WUniversity.sort(reverse=True)
KUniversity.sort(reverse=True)

#* 3번째 인덱스 값까지 더해서 출력
print(sum(WUniversity[:3]))
print(sum(KUniversity[:3]))