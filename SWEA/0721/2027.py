import sys

sys.stdin = open("2027.txt", "r")

# #++++
# +#+++
# ++#++
# +++#+
# ++++#
# 위의 내용을 출력

# 한 줄에 있는 갯수가 5
for i in range(5):
    for j in range(5):
        # i와 j가 같으면 # 출력
        if i == j:
            print('#', end = '')
        else:
            print('+', end = '')
    # 줄바꿈용 프린트
    print()