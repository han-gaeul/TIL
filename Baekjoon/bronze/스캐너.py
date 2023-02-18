# 3035

# 상근이는 매일 아침 영자 신문을 학교에 가져와서 읽는다
# 하지만 상근이의 눈은 점점 나빠졌고 더 이상 아침 신문을 읽을 수 없는 상황에 이르렀다
# 상근이는 스캐너를 이용해서 글자를 확대한 다음에 보려고 한다
# 신문 기사는 글자로 이루어진 R * C 행렬로 나타낼 수 있다
# 글자는 알파벳과 숫자, 그리고 마침표로 이루어져 있다
# 스캐너는 ZR과 ZC를 입력으로 받는다. 이렇게 되면 스캐너는 1 * 1크기였던
# 각 문자를 ZR * ZC 크기로 확대해서 출력한다
# 신문 기사와 ZR, ZC가 주어졌을 때 스캐너의 스캔을 거친 결과를 구하라

# 첫째 줄에 R, C, ZR, ZC가 주어진다
# 다음 R개 줄에는 신문 기사가 주어진다

# 스캐너에 스캔된 결과를 총 R * ZR개 줄에 걸쳐서 C * ZC개 문자씩 출력

R, C, ZR, ZC = map(int, input().split())
# 입력 받은 신문 기사를 저장하는 리스트
paper = []
# 스캔을 거친 결과를 저장하는 리스트
scanner = []
for _ in range(R):
    paper.append(input())
for i in range(R):
    # 신문 기사의 각 행 내용을 저장하는 리스트
    row = []
    for j in range(C):
        row.append(paper[i][j] * ZC)
    for _ in range(ZR):
        scanner.append(row)
for i in scanner:
    print(''.join(i))