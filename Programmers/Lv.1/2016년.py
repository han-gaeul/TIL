# 2016년 1월 1일은 금요일이다. 2016년 a월 b일은 무슨 요일일까?
# 두 수 a, b를 입력받아 2016년 a월 b일이 무슨 요일인지 return
# 요일의 이름은 일요일부터 토요일까지
# 각각 SUN, MON, TUE, WED, THU, FRI, SAT이다.
# 예를 들어 a = 5, b = 24라면 5월 24일은 화요일이므로
# 문자열 'TUE'를 return

def solution(a, b):
    # 일주일은 7일이고 1월 1일이 금요일이므로
    # 7로 나누었을 때 인덱스 1이 금요일로 나오게 함
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    # 2016년은 윤년인 조건이 있기 때문에 2월은 29일까지
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return day[(sum(month[:a-1]) + b) % 7]



import datetime

def solution(a, b):
    day = 'MON TUE WED THU FRI SAT SUN'.split()
    return day[datetime.datetime(2016, a, b).weekday]