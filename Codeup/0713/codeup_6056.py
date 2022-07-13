a, b = input().split()

c = bool(int(a))
d = bool(int(b))

if (bool(c and(not d)) or bool((not c) and d)):
    print("True")
else:
    print("False")