a = int(input("정수 a값 입력 : "))
b = int(input("정수 b값 입력 : "))
c = int(input("정수 c값 입력 : "))


def median(a, b, c):
    if (b >= a and c <= a) or (c < a and a < b):
        return a
    elif (a > b and c < b) or (c > b and b > a):
        return b
    return c


print(f"정수 {a, b, c}중 중앙값은 {median(a,b,c)}입니다.")
