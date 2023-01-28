# 신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로
# 발송하는 시스템을 개발하려 한다.
# 1. 각 유저는 한 번에 한 명의 유저를 신고할 수 있다
# 1-1. 신고 횟수에 제한은 없다. 서로 다른 유저를 계속해서 신고할 수 있다
# 1-2. 한 유저를 여러번 신고할 수도 있지만 동일한 유저에 대한 신고 횟수는 1회로 처리
# 2. k번 이상 신고된 유저는 게시판 이용이 정지되며 해당 유저를
# 신고한 모든 유저에게 정지 사실을 메일로 발송한다
# 2-1. 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에
# 게시판 이용 정지를 시키면서 정지 메일을 발송한다
# 이용자의 ID가 담긴 문자열 배열 id_list, 각 이용자가 신고한 이용자의
# ID 정보가 담긴 문자열 배열 report, 정지 기준이 되는 신고 횟수 k가
# 매개변수로 주어질 때 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}
    for i in set(report):
        a, b = i.split()
        reports[b] += 1
    for i in set(report):
        a, b = i.split()
        if reports[b] >= k:
            answer[id_list.index(a)] += 1
    return answer