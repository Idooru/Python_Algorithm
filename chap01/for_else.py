import random

while True:
    n = int(input('난수의 개수를 입력하세요 : '))

    if (3 < n < 10):
        break

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=' ')
    if r == 13:
        print('\n프로그램을 종료합니다.')
        break
else:
    print('\n난수 생성을 종료합니다.')