# 노트북 판매 대수에 상관없이 매년 임대료, 재산세, 보험료, 급여 등
# A만원의 고정 비용이 들며 한 대의 노트북을 생산하는 데에는
# 재료비와 인건비 등 총 B만원의 가변 비용이 든다고 한다
# 예) A = 1,000, B = 70이라고 하면
# 노트북을 한 대 생산하는 데는 총 1,070만원이 들며
# 열 대 생산하는 데는 총 1,700만원이 든다
# 노트북 가격이 C만원으로 책정 되었다고 한다
# 생산 대수를 늘려가다 보면 어느 순간 총 수입(판매비용)이
# 총 비용(=고정비용 + 가변비용)보다 많아지게 된다
# 최초로 총 수입이 총 비용보다 많아져 이익이 발생하는 지점을
# 손익분기점(BREAK-EVEN POINT)이라고 한다
# A, B, C가 주어졌을 때 손익분기점을 구하는 프로그램 작성

# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다
# A, B, C는 21억 이하의 자연수

# 첫 번째 줄에 손익분기점, 최초로 이익이 발생하는 판매량 출력
# 손익분기점이 존재하지 않으면 -1 출력

A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    print(int(A / (C - B) + 1))

# 생산하는 대 수를 n이라고 하면 A + B * n = C * n일 때
# 수입과 비용이 같아지기 때문에 B >= C일 경우
# 손익분기점이 나타나지 않게 되므로 걸러냄
# 생산되는 대수가 늘어날 때마다 C와 B의 차이만큼
# 수입과 비용의 차이가 줄어들게 되고
# 따라서 A / (C - B)대를 생산했을 때 수입과 비용이 같아지기 때문에
# +1부터 수입이 많아지게 된다