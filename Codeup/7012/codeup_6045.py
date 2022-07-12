a, b, c = input().split()

d_list = [int(a), int(b), int(c)]
result = sum(d_list)

avr = result/len(d_list)

print(result, format(avr, ".2f"))