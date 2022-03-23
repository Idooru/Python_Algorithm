def max_of(a):
    max = a[0]
    for i in range(1, len(a)):
        if a[i] > max:
            max = a[i]
    return max


arr = [1, 4, 3, 4.3, 2, 2.5, 3.4]

print(max_of(arr))