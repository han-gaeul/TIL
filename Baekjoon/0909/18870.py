# 수직선 위에 N개의 좌표 x1, x2, x3 ... xn이 있다
# 이 좌표에 좌표 압축을 적용하려고 한다
# xi을 좌표 압축한 결과 x'i의 값은 xi > xj 를 만족하는
# 서로 다른 좌표의 개수와 같아야 한다
# x1, x2, x3, ..., xn에 좌표 압축을 적용한 결과
# x'1, x'2, ..., x'n을 출력

# 첫째 줄에 N이 주어진다
# 둘째 줄에는 공백 한 칸으로 구분된 x1, x2, ..., xn이 주어진다

# 첫째 줄에 x'1, x'2, ..., x'n을 공백 한 칸으로 구분해 출력

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

# set 함수로 중복값 제거 후 정렬하고 리스트를 만듦
nums2 = sorted(list(set(nums)))
# nums를 순서대로 돌면서 새로 만든 nums2에서
# 해당 값을 인덱스를 뽑음
# 딕셔너리를 사용해 {dic[요소] : 요소의 Index} 형태로 저장해
dic = {nums2[i] : i for i in range(len(nums2))}

# dic[i]의 형태로 시간복잡도 O[1]로 답 출력
for i in nums:
    print(dic[i], end = ' ')