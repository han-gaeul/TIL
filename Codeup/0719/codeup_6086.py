num = int(input())

c = 0
sum = 0

while True:
    sum += c
    c += 1
    if sum >= num:
        break

print(sum)