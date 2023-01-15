# 연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5이다
# 두 정수 num과 total이 주어진다. 연속된 수 num개를 더한 값이
# total이 될 때, 정수 배열을 오름차순으로 담아 return

def solution(num, total):
    average =  total // num
    return [i for i in range(average - (num - 1) // 2, average + (num + 2) // 2)]



# 연속된 수이기 때문에 평균을 기준으로 좌측, 우측 끝 값을 구한다
# 좌, 우측 숫자의 개수는 num이 짝수냐 홀수냐에 따라 다르기 때문에
# 왼쪽 끝 값을 구하기 위해서는 num - 1로 하고
# 우측은 num + 2를 하면 짝수, 홀수를 구분하지 않고
# 연속적인 리스트를 구할 수 있다