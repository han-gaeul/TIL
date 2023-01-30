# 3009

# 세 점이 주어졌을 때 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾아라

# 세 점의 좌표가 한 줄에 하나씩 주어진다
# 좌표는 1보다 크거나 같고 1000보다 작거나 같은 정수

# 직사각형의 네 번째 점의 좌표를 출력

x_list = []
y_list = []
for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y = y_list[i]
print(x, y)