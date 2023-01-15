# 등차수열 혹은 등비수열 common이 매개변수로 주어질 때
# 마지막 원소 다음으로 올 숫자를 return

def solution(common):
    # 리스트의 3번째 요소까지 변수로 저장
    one, two, three = common[:3]
    # two에서 one을 뺀 것과 three에서 two를 뺀 값이 같다면
    # common은 등차수열
    if two - one == three - two:
        # common 마지막 요소에 차이만큼을 더한다
        answer = common[-1] + (two - one)
    # two에서 one을 나눈 몫이 three에서 two를 나눈 몫과 같다면
    # common은 등비수열
    elif two // one == three // two:
        # common 마지막 요소에 나눈 몫만큼을 곱한다
        answer = common[-1] * (two // one)
    return answer