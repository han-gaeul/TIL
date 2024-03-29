# △△ 게임대회가 개최되었다. 이 대회는 N명이 참가하고
# 토너먼트 형식으로 진행된다. N명의 참가자는 각각 1부터
# N번을 차례대로 배정 받는다. 그리고 1번<->2번, 3번<->4번,
# ..., N-1번<->N번의 참가자끼리 게임을 진행한다. 각 게임에서
# 이긴 사람은 다음 라운드에 진출할 수 있다. 이때, 다음 라운드에
# 진출할 참가자의 번호는 다시 1번부터 N/2번을 차례대로 배정받는다
# 만약 1번<->2번끼리 겨루는 게임에서 2번이 승리했다면 다음
# 라운드에서 1번을 부여받고, 3번<->4번에서 겨루는 게임에서
# 3번이 승리했다면 다음 라운드에서 2번을 부여받게 된다
# 게임은 최종 한 명이 남을 때까지 진행된다
# 이때, 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는
# B번 참가자와 몇번째 라운드에서 만나는지 궁금해졌다
# 게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 A, 경쟁자 번호 B가
# 매개변수로 주어질 때, 처음 라운드에서 A번을 가진 참가자는
# 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 return
# 단, A번 참가자와 B번 참가자는 서로 붙게 되기 전까지
# 항상 이긴다고 가정한다

def solution(N, A, B):
    # 라운드 수를 저장할 변수
    answer = 0
    # A와 B가 만날 때까지 반복
    while A != B:
        # 라운드 수 증가
        answer += 1
        # A와 B를 다음 라운드에 배정된 번호로 업데이트
        A, B = (A + 1) // 2, (B + 1) // 2
    return answer



# 이 함수는 주어진 참가자 수 N, 참가자 A와 B의 번호를 토대로
# A와 B가 만날 때까지 진행한 라운드 수를 계산하는 함수이다.
# while문을 사용해 A와 B가 만날 때까지 반복해서
# 반복할 때마다 라운드 수를 1씩 증가시키고, A와 B를 다음
# 라운드에 배정된 번호로 업데이트 한다.

# 문제에서 말하는 게임 대회의 진행 방식은 이진 트리 형태로
# 나타낼 수 있다. 각 노드는 한 명의 참가자를 나타내며, 루트
# 노드에서 시작해 각 레벨에서는 이전 레벵에서 이긴 참가자들끼리
# 대결하게 된다. 이진 트리에서 같은 레벨에 위치한 두 노드가
# 대결을 하면, 그들은 같은 레벨에서 이긴 참가자가 되고 다음
# 라운드에서는 같은 부모 노드의 두 자식 노드가 된다. 이를 토대로
# 문제에서 주어진 조건을 적용하면, A와 B가 만날 때까지 대결을
# 반복하는 것은 결국 A와 B가 같은 부모 노드를 가지게 되는
# 상황을 의미한다.
# 따라서, A와 B가 만날 때까지 대결하는 과정에서 A와 B가 위치한
# 노드가 다음 라운드에서는 같은 부모 노드를 가지게 되는 것이다
# 이를 구현하기 위해서는 A와 B가 다음 라운드에서 어떤 참가자들과
# 대결할 것인지를 계산해야 한다. 이진 트리에서는 같은 부모 노드를
# 가지는 두 자식 노드의 번호는 각각 (N + 1) // 2와 N / 2로 
# 계산할 수 있다.
# 이를 바탕으로, A와 B가 다음 라운드에서 배정받을 번호를 계산하고
# 계속해서 업데이트해 나가면 A와 B가 만날 때까지 대결한 라운드
# 수를 계산할 수 있다.