n = int(input("몇개?"))
w = int(input("몇줄?"))

for i in range(n):
    print('*', end='')

    if i % w == w - 1:
        print()