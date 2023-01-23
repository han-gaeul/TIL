# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 return
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미한다
# 1은 소수가 아니다

def solution(n):
    # 2부터 n까지의 숫자들을 set 형태로 저장
    num = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in num:
            # 2 * i부터 n까지 i의 배수들을 set 형태로 num에서 제거
            num -= set(range(2 * i, n + 1, i))
    return len(num)


# 에라토스테네스의 체(Eratosthenes' sieve)
# 2부터 n까지의 숫자들 중 소수를 구하는 알고리즘
# 1. 2부터 n까지의 숫자들을 저장하는 배열을 만든다
# 2. 2부터 n까지의 숫자를 하나씩 검사한다
# 3. 검사하는 숫자가 소수라면 그 숫자의 배수들을 모두 제거한다
# 4. 2부터 n까지 검사하며 아직 제거되지 않은 숫자들이 소수이다
# 간단하지만 효율적인 알고리즘으로 소수를 구하는데 사용된다

# n까지의 모든 소수를 구한다고 하면 2를 제외한 모든 2의 배수를 num에서 제거
# 3을 제외한 모든 3의 배수를 제거. 4는 2의 배수에서 제거됨
# 5를 제외한 모든 5의 배수를 제거.
# 이렇게 반복해서 num에 남아 있는 수들이 소수이다.