# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다
# 회원들을 나이가 증가하는 순으로 나이가 같으면
# 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램 작성

# 첫째 줄에 온라인 저지 회원의 수 N이 주어진다
# 둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다

# 첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순
# 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을
# 공백으로 구분해 출력한다

N = int(input())
member_list = []

for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    member_list.append((age, name))

# (age, name)에서 age만 비교
member_list.sort(key = lambda x : x[0])

for i in member_list:
    print(i[0], i[1])