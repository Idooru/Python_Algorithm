a = int(input("정수 a값 입력 : "))
b = int(input("정수 b값 입력 : "))
sum = 0

if a > b:
    a, b = b, a

for i in range(a, b + 1):
    sum += i

print(f"{a}부터 {b}까지의 합은 {sum}")
