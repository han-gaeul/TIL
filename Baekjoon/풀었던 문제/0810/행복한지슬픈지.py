# 10769
# 승엽이가 보내는 이모티콘은 세 개의 문자가 붙어있는 구조로
# 행복한 얼굴을 나타내는 :-)와 슬픈 얼굴을 나타내는 :-(가 있다

# 출력은 다음 규칙에 따라 정해진다
# 어떤 이모티콘도 포함되어 있지 않으면 none 출력
# 행복한 이모티콘과 슬픈 이모티콘의 수가 동일하면 unsure 출력
# 행복한 이모티콘이 슬픈 이모티콘보다 많이 포함되어 있으면 happy 출력
# 슬픈 이모티콘이 행복한 이모티콘보다 많이 포함되어 있으면 sad 출력

import sys
sys.stdin = open('행복한지슬픈지.txt')

text = input()

#* 입력 받은 문자에서 이모티콘 수 세기
textHappy = text.count(':-)')
textSad = text.count(':-(')

#* 만약 이모티콘이 없다면
if textHappy == 0 and textSad == 0:
    print('none')
#* 이모티콘 수가 같으면
elif textHappy == textSad:
    print('unsure')
#* 행복 이모티콘이 슬픈 이모티콘보다 많으면
elif textHappy > textSad:
    print('happy')
#* 슬픈 이모티콘이 행복 이모티콘보다 많으면
elif textSad > textHappy:
    print('sad')