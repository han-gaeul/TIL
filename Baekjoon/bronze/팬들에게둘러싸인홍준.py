# 14581

# 홍준은 참 팬이 많다. 이를 본 구사과는 BOJ 슬랙에서 이모티콘을 만들었다
# 선풍기 모양의 이모티콘은 :fan:이고, 홍준의 이모티콘은 :(홍준의 아이디):이다
# 홍준의 아이디가 주어지면 구사과가 만든 이모티콘을 출력하라

# 첫번째 줄에 홍준의 아이디를 입력받는다
# 홍준의 아이디는 알파벳 소문자, 대문자, 숫자로만 이루어져 있다

# 3개의 줄에 걸쳐 팬들에게 둘러싸인 홍준의 모습을 출력



# 1.
hj_id = input()
fan = [[':fan:' for _ in range(3)] for _ in range(3)]
fan[1][1] = f':{hj_id}:'
print('\n'.join([''.join(i) for i in fan]))


# 2.
hj_id = input()
print(':fan::fan::fan:')
print(f':fan::{hj_id}::fan:')
print(':fan::fan::fan:')