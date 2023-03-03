# 14889

# 오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다
# 축구는 평일 오후에 하고 의무 참석도 아니다
# 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다
# 이제 N / 2명으로 이루어진 스타트팀과 링크팀으로 사람들을 나눠야 한다
# BOJ를 운영하는 회사답게 사람에게 번호를 1부터 N까지로 배정했고 아래와 같은 능력치를 조사했다
# 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때 팀에 더해지는 능력치이다
# 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다
# Sij는 Sji와 다를 수도 있으며 i번 사람과 j번 사람이 같은 팀에 속했을 때
# 팀에 더해지는 능력치는 Sij와 Sji이다
# N = 4이고 S가 아래와 같은 경우를 살펴보자
# 예를 들어 1, 2번이 스타트팀, 3, 4번이 링크팀에 속한 경우 두 팀의 능력치는 아래와 같다
# 스타트팀 : S12 + S21 = 1 + 4 = 5
# 링크팀 : S34 + S43 = 2 + 5 = 7
# 1, 3번이 스타트팀, 2, 4번이 링크팀에 속하면 두 팀의 능력치는 아래와 같다
# 스타트팀 : S13 + S31 = 2 + 7 = 9
# 링크팀 : S24 + S42 = 6 + 4 = 10
# 축구를 재미있게 하기 위해서 스타트팀의 능력치와 링크팀의 능력치의 차이를 최소로 하려고 한다
# 위의 예제와 같은 경우에는 1, 4번이 스타트팀, 2, 3번이 링크팀에 속하면
# 스타트팀의 능력치가 6, 링크팀의 능력치가 6이 되어서 차이가 0이 되고 이 값이 최소이다

# 첫째 줄에 N이 주어진다
# 둘째 줄부터 N개의 줄에 S가 주어진다
# 각 줄은 N개의 수로 이루어져 있고 i번 줄의 j번째 수는 Sij이다
# Sii는 항상 0이다

# 첫째 줄에 스타트팀과 링크팀의 능력치 차이의 최솟값 출력


# 1.
from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
team = []
for add in list(combinations(members, N // 2)):
    team.append(add)
minimum = 10000
for i in range(len(team) // 2):
    team_A = team[i]
    team_A_point = 0
    for j in range(N // 2):
        member = team[j]
        for k in team:
            team_A_point += S[member][k]
    team_B = team[-i - 1]
    team_B_point = 0
    for j in range(N // 2):
        member = team[j]
        for k in team:
            team_B_point += S[member][k]
    minimum = min(minimum, abs(team_A_point- team_B_point))
print(minimum)
# 런타임에러
# why...?


# 2.
from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
possible_team = []
for team in list(combinations(members, N//2)):
    possible_team.append(team)
min_stat_gap = 10000
for i in range(len(possible_team)//2):
    team = possible_team[i]
    stat_A = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_A += S[member][k]
    team = possible_team[-i-1]
    stat_B = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_B += S[member][k]    
    min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B))
print(min_stat_gap)