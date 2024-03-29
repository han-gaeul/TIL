# 머쓱이는 친구에게 모스부호를 이용한 편지를 받았다
# 그냥은 읽을 수 없어 이를 해독하는 프로그램을 만들려고 한다
# 문자열 letter가 매개변수로 주어질 때
# letter를 영어 소문자로 바꾼 문자열을 return

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    letter = letter.split(' ')
    answer = []
    for i in letter:
        answer.append(morse[i])
    return ''.join(answer)


def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    return ''.join([morse[i] for i in letter.split(' ')])