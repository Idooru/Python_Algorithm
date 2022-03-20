def med3(a, b, c):
    if (b >= a and c <= a) or (a >= c and b <= a):
        return a
    elif (a > b and b < c) or (c > b and a < b):
        return b
    return c


a = int(input("정수 a의 값을 입력하세요 : "))
b = int(input("정수 b의 값을 입력하세요 : "))
c = int(input("정수 c의 값을 입력하세요 : "))

print(f"세 정수의 중앙값은 {med3(a, b, c)}입니다.")
