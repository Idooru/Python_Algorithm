def ascending(end, start):
    arr = []
    for i in range(start, end + 1):
        arr.append(i)

    return arr[0], arr[len(arr) - 1]


a = int(input("a : "))
b = int(input("b : "))

if a > b:
    a, b = ascending(a, b)

print(a, b)