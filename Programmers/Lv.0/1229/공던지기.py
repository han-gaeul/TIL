# 머쓱이는 친구들과 동그랗게 서서 공 던지기 게임을 하고 있다
# 공은 1번부터 던지며 오른쪽을 한 명을 건너뛰고
# 그다음 사람에게만 던질 수 있다
# 친구들의 번호가 들어있는 정수 배열 numbers와
# 정수 K가 주어질 때 k번째 공을 던지는 사람의 번호를 return

def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]