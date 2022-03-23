a = int(input("정수 a의 값을 입력하세요 : "))
b = int(input("정수 b의 값을 입력하세요 : "))
c = int(input("정수 c의 값을 입력하세요 : "))

max = a
if max < b:
    max = b
if max < c:
    max = c

print(f"최댓값은 {max}입니다.")
