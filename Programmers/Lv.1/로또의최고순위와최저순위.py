# 로또6/45(이하 '로또')는 1부터 45까지의 숫자 6개를 찍어서
# 맞히는 대표적인 복권이다. 아래는 로또의 순위를 정하는 방식이다
# 순위 당첨내용
# 1 6개 번호가 모두 일치
# 2 5개 번호가 일치
# 3 4개 번호가 일치
# 4 3개 번호가 일치
# 5 2개 번호가 일치
# 6(낙첨) 그 외
# 로또를 구매한 민우는 당첨 번호 발표일을 학수고대하고 있다
# 하지만 민우의 동생이 로또에 낙서를 하여 일부 번호를 알아볼 수 없게 됐다
# 당첨 번호 발표 후 민우는 자신이 구매했던 로또로 당첨이 가능했던
# 최고 순위와 최저 순위를 알아보고 싶어졌다
# 알아볼 수 없는 번호를 0으로 표기하기로 하고 민우가 구매한
# 로또 번호 6개가 44, 1, 0, 0, 31, 25라고 가정해보자
# 당첨 번호 6개가 31, 10, 45, 1, 6, 19라면 당첨 가능한 최고 순위와
# 최저 순위의 한 예는 아래와 같다
# 당첨 번호	31	10	45	1	6	19	결과
# 최고 순위 번호	31	0→10	44	1	0→6	25	4개 번호 일치, 3등
# 최저 순위 번호	31	0→11	44	1	0→7	25	2개 번호 일치, 5등
# 순서와 상관없이 구매한 로또에 당첨 번호와 일치하는 번호가 있으면
# 맞힌 걸로 인정된다
# 알아볼 수 없는 두 개의 번호를 각각 10, 6이라고 가정하면 3등 당첨
# 3등을 만드는 다른 방법도 존재하지만 2등 이상으로는 만들 수 없음
# 알아볼 수 없는 두 개의 번호를 각각 11, 7이라고 가정하면 5등 당첨
# 5등을 만드는 다른 방법도 존재하지만 6등(낙첨)으로 만들 수 없음
# 민우가 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은
# 배열 win_nums가 매개변수로 주어진다
# 이때 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아 return



# 1.
def solution(lottos, win_nums):
    # 당첨 가능한 최저 개수
    # lottos 리스트에 있는 번호 중
    # win_nums 리스트에 있는 번호의 개수를 저장
    count_win = 0
    # 알아볼 수 없는 번호의 개수
    # lottos 리스트에 있는 번호 중 0인 번호의 개수를 저장
    count_zero = 0
    for i in range(6):
        if lottos[i] in win_nums:
            count_win += 1
        elif lottos[i] == 0:
            count_zero += 1
    # 당첨 가능한 최고 개수
    # 알아볼 수 없는 번호의 개수와 당첨 가능한 개수를 더함
    total = count_zero + count_win
    # 당첨 순위
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    return [rank[total], rank[count_win]]



# 2.
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    count_0 = lottos.count(0)
    answer = 0
    for i in win_nums:
        if i in lottos:
            answer += 1
    return rank[count_0 + answer], rank[answer]