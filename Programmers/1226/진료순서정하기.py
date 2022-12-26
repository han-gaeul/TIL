# 외과의사 머쓱이는 응급실에 온 환자의
# 응급도를 기준으로 순서를 정하려고 한다.
# 정수 배열 emergency가 매개변수로 주어질 때
# 응급도가 높은 순서대로 진료 순서를 정한 배열을 return

def solution(emergency):
    # 주어진 배열의 길이만큼 숫자 1일 담긴 배열 생성
    answer = [1] * len(emergency)
    # 주어진 배열의 길이만큼 순차적으로 탐색
    for index in range(0, len(emergency)):
        # 배열을 한 번 더 탐색
        for number in emergency:
            # 두번째 탐색중인 숫자보다 첫번째 탐색중인 숫자가 더 크다면
            if emergency[index] < number:
                # answer 배열의 첫번째 탐색중인 요소의 인덱스에 +1
                answer[index] += 1
    return answer