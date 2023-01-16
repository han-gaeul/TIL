# X 대학 M 교수님은 프로그래밍 수업을 맡고 있다
# 교실엔 학생 30명이 있는데 학생 명부엔 각 학생별로
# 1번부터 30번까지 출석 번호가 붙어있다
# 교수님이 내준 특별과제를 28명이 제출 했는데
# 그 중에서 제출을 하지 않은 학생 2명의 출석번호를 구하라

# 입력은 총 28줄로 각 제출자(학생)의 출석번호가 한 줄에 하나씩 주어진다
# 출석번호에 중복은 없다


# 1.
students = [i for i in range(1, 31)]

for _ in range(28):
    students.remove(int(input()))

print(*students, sep='\n')


# 2.
students = [int(input()) for i in range(28)]

for i in range(1, 31):
    if i not in students:
        print(i)