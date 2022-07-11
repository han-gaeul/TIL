
# 결과를 동시에 할당
a, b = input().split() # numbers = input().split()
a = int(a) # a = int(numbers[0])
b = int(b) # b = int(numbers[1])
print(a) # print(int(a))
print(b) # print(int(b))


# 고급 방법 -> 수요일에 떠먹여주심 와압-0-
a, b = map(int, input().split())
print(a, type(a))
print(b, type(b))