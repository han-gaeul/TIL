# 첫째 줄에 테스트 케이스의 개수 C가 주어진다
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N이 주어지고
# 이어서 N명의 점수가 주어진다

# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여
# 소수점 셋째 자리까지 출력

N = int(input())

for _ in range(N):
    score = list(map(int, input().split()))
    # 평균을 구하기 위해 1번째 요소부터 마지막까지 더한 다음
    # 학생 수인 score[0]으로 나누고 변수 avg에 저장
    avg = sum(score[1:]) / score[0]
    
    # 평균을 넘는 학생의 수를 세기 위해 count 정의
    count = 0

    # for문을 사용해 1번째 요소부터 평균이 넘는지 확인
    for i in score[1:] :
        if i > avg:
            count += 1

    # count를 학생의 수인 score[0]으로 나누고 100을 곱한다
    percent = (count / score[0] * 100)
    # '%.3f'를 하여 percent의 소수점 3번째까지만 출력
    print('%.3f' % percent + '%')