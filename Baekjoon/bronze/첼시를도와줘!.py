# 11098

# 구단이 성적을 내지 못한다면 답은 새 선수 영입 뿐이다.
# 이것은 오늘날 유럽 리그에서 가장 흔한 전략이고 노르웨이의 로젠버그 팀은 이러한 전략이 성공한 대표적 예시
# 그들은 많은 스카우터들을 지구 곳곳에 파견해 가능성 있는 루키를 찾는다
# 현재 첼시는 프리미어 리그에서 헤매고 있고 결국 새로운 선수를 사기로 결정했다
# 하지만 그들은 스카우터를 기다리기 지쳤고 훨씬 더 효율적인 전략을 개발해냈다
# '만약 무언가 팔리고 있다면, 그것에는 합당한 이유가 있다'는 배룸의 명언이 바로 그것이다
# 축구에서 이 말은 곧 가장 비싼 선수가 가장 좋은 선수라는 얘기가 된다
# 이에 따라 새로운 선수를 찾는 방법은 단순히 구단들에게 전화를 걸어
# 그들의 가장 비싼 선수를 사는게 되었다
# 첼시가 리스트에서 가장 비싼 선수를 찾아낼 수 있게 돕자

# 첫 번째 줄에는 테스트 케이스의 개수 n이 주어진다
# 각 테스트 케이스의 첫 번째 줄 p는 고려해야할 선수의 수이다
# 그 아래 p개의 줄에는 선수의 정보가 표시된다
# 각각의 줄은 선수의 가격 C와 이름을 입력
# 모든 선수의 가격은 서로 다르다

# 각각의 테스트 케이스에서 가장 비싼 선수의 이름을 출력

n = int(input())
for _ in range(n):
    li = []
    p = int(input())
    for __ in range(p):
        C, name = input().split()
        li.append([int(C), name])
    li.sort()
    print(li[-1][1])