h, b, c, s = map(int, input().split())
# print(round(h * b * c * s / 8 / 1024 / 1024, 1), 'MB')
print('%.1f'%(h * b * c * s / 8 / 1024 / 1024), 'MB')

# h = 강약 체크. b = 저장 비트 수,  c = 트랙 개수, s = 녹음 시간
# 저장 용량은 강약 체크한 수, 채널, 비트 사용 개수, 녹음 시간에 비례
# 문제를 풀기 위해 bit를 MB로 바꾸어야 함

# 저장 용량 = h * b * c * s 를 구한 후 bit 단위를 MB로 변환
# 우선 h * b * c * s 를 x 라고 생각
# 8 bit는 1byte 이므로 bit로 표현된 x 를 byte로 나타내기 위해 8로 나눔
# 1024byte는 1KB 이므로 byte로 표현된 x / 8 을 1024로 나눔
# 1024KB는 1MB 이므로 KB로 표현된 x를 1024로 다시 나눔

# 요약
# bit 단위 저장 용량 = h * b * c * s
# byte 단위 저장 용량 = h * b * c * s / 8
# KB 단위 저장 용량 = h * b * c * s / 8 / 1024
# MB 단위 저장 용량 = h * b * c * s / 8 / 1024 / 1024