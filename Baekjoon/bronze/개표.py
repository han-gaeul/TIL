# 10102

# A와 B가 한 오디션 프로의 결승전에 진출했다
# 결승전의 승자는 심사위원의 투표로 결정된다
# 심사위원의 투표 결과가 주어졌을 때 어떤 사람이 우승하는지 구하라

# 입력은 총 두 줄로 이루어져 있다
# 첫째 줄에는 심사위원의 수 V가 주어지고 둘째 줄에는 각 심사위원이 누구에게 투표했는지 주어진다
# A와 B는 각각 그 참가자를 나타낸다

# A가 받은 표가 B보다 많은 경우 A,
# B가 받은 표가 A보다 많은 경우 B,
# 같은 경우 Tie 출력

V = int(input())
vote = list(str(input()))
if vote.count('A') > vote.count('B'):
    print('A')
elif vote.count('A') < vote.count('B'):
    print('B')
else:
    print('Tie')