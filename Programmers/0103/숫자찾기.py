# 정수 num과 k가 매개변수로 주어질 때
# num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는
# 자리 수를 반환하고 없으면 -1을 반환


def solution(num, k):
    num_str = str(num)
    if str(k) not in num_str:
        return -1
    return num_str.index(str(k)) + 1