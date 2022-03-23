def max_of(a):
    max = a[0] 
    for i in range(1, len(a)):
        if a[i] > max:
            max = a[i]

    return max
if __name__ == "__main__":
    print("Hello")