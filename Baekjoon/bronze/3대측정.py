# 20299

# 웨이트 트레이닝에서의 3대 측정은 스쿼트, 벤치프레스, 데드리프트의 중량을 측정하는 것이다
# 하지만 세 명이 한 팀을 이뤄 출전하는 전국 대학생 프로그래밍 대회(ICPC)의 참가자들은
# 다소 독특한 방법으로 3대를 측정하는데 바로 팀원 각각의 실력을 수치로 나타내는 '코드포스 레이팅'을 비교하는 것이다
# 웨이트 트레이닝계에는 3대 중량을 합쳐 500kg를 넘지 못하는 사람은 '언더아머' 브랜드의
# 옷을 입지 못한다는 암묵적인 룰이 있으며 이들을 단속하는 '언더아머 단속반'이 존재한다는 소문도 있다
# sogang ICPC Team은 이를 벤치마킹해 팀원 3명의 코드포스 레이팅의 합이 K 미만인 팀은
# 가입할 수 없는 VIP 클럽을 만들고자 한다
# 하지만 이런 조건에서는 세 명 중 한 명의 레이팅이 현저히 낮더라도 나머지 두 명의 레이팅이
# 충분히 높다면 세 명이 모두 VIP 클럽에 가입할 수 있게 된다
# 클럽에 가입하는 사람들은 모두 일정 수준 이상이어야겠다고 판단한 학회장 임지환은
# 모든 팀원의 레이팅이 L 이상이고 팀원 세명의 레이팅의 합이 K 이상인 팀만이 가입할 수 있게 했다
# 학회 일과 연합 일에 치여 사는 지환이는 VIP 클럽의 회원 관리까지 할 시간이 없다
# 지환이를 위해 지원자 중 VIP 클럽에 가입할 수 있는 팀의 수를 구하고
# VIP 회원들의 레이팅을 출력

# 첫째 줄에 정수 N, K, L이 주어진다.
# N은 팀의 수, K는 팀원 3명의 레이팅 합에 대한 클럽 가입 조건,
# L은 개인 레이팅에 대한 클럽 가입 조건이다
# 둘째 줄부터 N개의 줄에 VIP 클럽에 신청한 팀의 팀원들의 레이팅 정보를
# 나타내는 정수 x1, x2, x3이 한 줄에 한 팀씩 주어진다

# 첫째 줄에 VIP 클럽에 가입이 가능한 팀의 수를 출력
# 둘째 줄에 VIP 회원들의 레이팅을 입력받은 순서대로 공백으로 구분해 하나씩 출력

import sys

N, K, L = map(int, sys.stdin.readline().split())
cnt = 0
li = []
for _ in range(N):
    team = list(map(int, sys.stdin.readline().split()))
    check = True
    for i in team:
        if i < L:
            check = False
            break
    if check:
        if sum(team) >= K:
            li.extend(team)
            cnt += 1
print(cnt, *li, sep='\n')


# 팀원들의 점수가 L 이하인 경우 해당 팀은 탈락
# 또한 팀원들의 총점이 K 이상인 경우에만 해당 팀 선발
