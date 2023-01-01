# 영어가 싫은 머쓱이는 영어로 표기되어 있는 숫자를
# 수로 바꾸려고 한다
# 문자열 numbers가 매개변수로 주어질 때
# numbers를 정수로 바꿔 return

def solution(numbers):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for index, num in enumerate(nums):
        numbers = numbers.replace(num, str(index))
    return int(numbers)


# enumerate()
# 리스트의 원소에 순서값을 부여해주는 함수
# 입력으로 받은 데이터와 인덱스 값을 포함하는 객체를 반환
# 예)
# nums  = ['zero', 'one', 'two']
# for num in enumerate(nums):
#     print(num)
# (0, 'zero')
# (1, 'one')
# (2, 'two')