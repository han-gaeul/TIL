# 5635

# 어떤 반에 있는 학생들의 생일이 주어졌을 때 가장 나이가 적은 사람과 가장 많은 사람을 구하라

# 첫째 줄에 반에 있는 학생의 수 n이 주어진다
# 다음 n개의 줄에는 각 학생의 이름과 생일이 '이름 dd mm yyyy'와 같은 형식으로 주어진다
# 이름은 그 학생의 이름이며 dd mm yyyy는 생일 일, 월, 연도이다
# 이름이 같거나 생일이 같은 사람은 없다

# 첫째 줄에 가장 나이가 적은 사람의 이름
# 둘째 줄에 가장 나이가 많은 사람의 이름을 출력

n = int(input())
li = []
for _ in range(n):
    student = input().split()
    student[1:] = map(int, student[1:])
    li.append(student)
li.sort(key=lambda student : (student[3], student[2], student[1]))
print(li[-1][0], li[0][0], sep='\n')