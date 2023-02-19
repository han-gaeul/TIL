# 4470

# 텍스트에서 줄을 입력받은 뒤 줄 번호를 출력

# 첫째 줄에 줄의 수 N이 주어진다
# 둘째 줄부터 N개의 줄에 각 줄의 내용이 주어진다
# 각 줄에 있는 글자의 개수는 50글자를 넘지 않는다

# 각 문장의 앞에 줄 번호를 추가한 뒤 출력
# 줄 번호는 1번부터 시작한다
# 줄번호를 추가하는 형식은 출력 예제를 참고

N = int(input())
for i in range(1, N + 1):
    content = input()
    print(f'{i}. {content}')