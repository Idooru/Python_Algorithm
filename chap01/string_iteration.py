def stringIter(char, number, line):

    for i in range(1, number + 1):
        print(char, end='')
        if number % i == line:
            print()


n = int(input("몇 개를 출력할지 입력하세요 : "))
w = int(input("몇 개마다 줄바꿈할지 입력하세요 : "))
c = input('문자를 입력하세요(1글자) : ')

stringIter(c, n, w)