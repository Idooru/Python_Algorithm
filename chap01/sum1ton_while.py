n = int(input('정수를 입력하세요 : '))
i = 0
sum = 0

while (i <= n):
    sum += i
    i += 1

print(f'1부터 {n}까지 합은 {sum}')
print(f'i값은 {i}입니다.')