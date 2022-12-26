# 우주여행을 하던 머쓱이는 엔진 고장으로
# PROGRANMMERS-962 행성에 불시착했다.
# 입국심사에서 나이를 말해야 하는데
# 행성에서는 나이를 알파벳으로 말한다.
# a는 0, b는 1, c는 2, ..., j는 9이다.
# 예를 들어 23살은 cd, 51살은 fb로 표현
# age가 매개변수로 주어질 때 나이를 return


# 리스트
def solution(age):
    answer = ''
    word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for i in str(age):
        answer += word[int(i)]
    return answer

# 아스키코드
def solution(age):
    answer = ''
    return answer.join([chr(int(i) + 97) for i in str(age)])