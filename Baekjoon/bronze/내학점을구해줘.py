# 10984

# 게으른 근우는 열심히 놀다가 문득 자신의 학점 평균이 얼마일지 궁금해졌다

# 첫 번째 줄에 학기의 수 T가 주어진다
# 두 번째 줄부터 T개 학기에 대한 정보가 주어진다
# 각 학기에 대한 정보는 다음과 같이 구성되어 있다
# 첫 번째 줄에 들었던 과목의 수 N이 주어지고 다음 N개 줄에 걸쳐 N개 과목들의 학점 C와 성적 G가 주어진다
# G는 {0, 0.7, 1, 1.3, 1.7, 2, 2.3, 2.7, 3, 3.3, 3.7, 4, 4.3} 중 하나미여 소수 부분은 최대 한 자리까지 주어진다

# 각 학기에 대해 근우의 총 학점과 평점(GPA)를 출력

T = int(input())
for _ in range(T):
    N = int(input())
    G = 0.0
    C = 0
    for i in range(N):
        c, g = map(float, input().split())
        G += c * g
        C += c
    print('%d %.1f' % (int(C), G / C))