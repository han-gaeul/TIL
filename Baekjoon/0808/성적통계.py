# 5800
# 각 반의 학생들의 수학 시험 성적이 주어졌을 때
# 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램 작성

# 첫째 줄에 반의 개수 K가 주어진다
# 다음 K개 줄에는 각 반의 학생수 N과 각 학생의 수학 성적이 주어진다

# 출력은 다음과 같이 두 줄로 이루어져 있다
# 첫째 줄에는 'Class X'를 출력
# X는 반의 번호이며 입력으로 주어진 순서대로 1부터 증가
# 둘째 줄에는 가장 높은 점수, 낮은 점수, 성적을 내림차순으로
# 정렬했을 때 가장 큰 인접한 점수 차이를 예제 출력과 같은 형식으로 출력

# 출력 예시
# Class 1
# Max 78, Min 23, Largest gap 46
# Class 2
# Max 99, Min 25, Largest gap 25

import sys
sys.stdin = open('성적통계.txt')

K = int(input())

for i in range(K):
    students = list(map(int, input().split()))
    #* 0번 인덱스에 있는 학생 수 삭제
    del students[0]
    #* 리스트 정렬
    students.sort()
    gap = []
    print('Class', i + 1)

    for j in range(len(students) - 1):
        #* 뒤에 있는 인덱스 값에서 앞 인덱스 값을 빼고 gap에 추가
        gap.append(students[j + 1] - students[j])

    print('Max', str(max(students)) + ',', 'Min', str(min(students)) + ',', 'Largest gap', max(gap))