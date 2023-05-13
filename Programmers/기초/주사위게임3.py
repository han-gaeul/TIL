# 1부터 6까지 숫자가 적힌 주사위가 네개 있다
# 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은
# 점수를 얻는다
# 네 주사위에서 나온 숫자가 모두 같다면 1111 x p점을 얻는다
# 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서
# 나온 숫자가 q(p != q)라면 (10 x p + q)제곱점을 얻는다
# 주사위가 두개씩 같은 값이 나오고 나온 숫자를 각각
# p와 다른 q, rdlfkaus q x r점을 얻는다
# 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장
# 작은 숫자만큼의 점수를 얻는다
# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수
# a, b, c, d로 주어질 때 얻는 점수를 반환

import functools

def solution(a, b, c, d):
    dices = [a, b, c, d]
    num_frequency = {}
    
    for num in dices:
        if num in num_frequency:
            num_frequency[num] += 1
        else:
            num_frequency[num] = 1
    
    val_info = list(num_frequency.values())
    key_info = list(num_frequency.keys())

    count_val = max(val_info)
    
    if count_val == 4:
        return a * 1111
    elif count_val == 3:
        three_key = key_info[val_info.index(3)]
        one_key = key_info[val_info.index(1)]
        return (10 * int(three_key) + int(one_key))**2
    elif count_val == 2:
        if len(key_info) == 2:
            if a == b:
                return (a + c) * abs(a - c)
            else:
                return (a + b) * abs(a - b)
        else:
            return functools.reduce(lambda acc, cur: acc * int(cur) if num_frequency[cur] == 1 else acc, key_info, 1)
    else:
        return min(a, b, c, d)