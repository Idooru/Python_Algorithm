from ssearch_while import seq_search

print('실수를 검색합니다.')
print('주의: "End"를 입력하면 종료합니다.')

number = 0
x = []

while True:
    s = input(f'x[${number}]: ')
    if s == "End":
        break
    x.append(float(s))
    number += 1

target = float(input('검색하려는 값을 입력하세요.: '))
idx = seq_search(x, target)

if idx == -1:
    print(False)

else:
    print(f'검색하려는 값({target})은 x[{idx}]에 존재합니다.')
