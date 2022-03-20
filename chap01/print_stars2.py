n = int(input("몇 개를 출력할지 입력하세요 : "))
w = int(input("몇 개마다 줄바꿈할지 입력하세요 : "))

for _ in range(n // w):
    print("*" * w)

rest = n % w

if rest:
    print('*' * rest)
