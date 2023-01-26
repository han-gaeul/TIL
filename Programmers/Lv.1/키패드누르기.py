# 스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀있다
# 이 전화 키패드에서 왼손과 오른손의 엄지 손가락만을 이용해서
# 숫자만을 입력하려고 한다
# 맨 처음 왼손 엄지 손가락은 * 키패드에, 오른손 엄지 손가락은
# # 키패드 위치에서 시작하며 엄지 손가락을 사용하는 규칙은 다음과 같다
# 1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며
# 키패드 이동 한 칸은 거리로 1에 해당한다
# 2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지 손가락을 사용
# 3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지 손가락을 사용
# 4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지 손가락의
# 현재 키패드의 위치에서 더 가까운 엄지 손가락을 사용
# 4-1 만약 두 엄지손가락의 거리가 같다면 오른손잡이는 오른손 엄지 손가락,
# 왼손잡이는 왼손 엄지 손가락을 사용
# 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인지를
# 나타내는 문자열 hand가 매개변수로 주어질 때
# 각 번호를 누른 엄지 손가락이 왼손인지 오른손인지를 나타내는
# 연속된 문자열 형태로 return

def solution(numbers, hand):
    answer = ''
    # '*' 을 10, 0을 11, '#'을 12로 가정하고
    # 각 엄지손가락의 시작 위치 지정
    lastL = 10
    lastR = 12
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            lastL = i
        elif i in [3, 6, 9]:
            answer += 'R'
            lastR = i
        else:
            i = 11 if i == 0 else i
            
            # 각 엄지손가락과 현재 숫자 사이의 거리 계산
            absL = abs(i - lastL)
            absR = abs(i - lastR)
 
            # 각 엄지손가락의 거리를 비교해서 더 가까운 손가락 추가
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer += 'R'
                lastR = i
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer += 'L'
                lastL = i
            else:
                # 거리가 같을 경우 어느손 잡이인지에 따라 손가락 추가
                if hand == 'left':
                    answer += 'L'
                    lastL = i
                else:
                    answer += 'R'
                    lastR = i
    return answer