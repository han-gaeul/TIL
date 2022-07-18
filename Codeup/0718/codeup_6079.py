from curses import beep


num = int(input())

count = 0

for i in range(1000):
    count = count + i
    if count >= num:
        print(i)
        break