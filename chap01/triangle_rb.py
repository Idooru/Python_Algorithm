n = int(input("짧은 변의 길이를 입력하세요 : "))

for i in range(n):
    for _ in range(n - i - 1):
        print(' ', end='')
    for _ in range(i + 1):
        print('*', end='')
    print()