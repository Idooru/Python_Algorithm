from max import max_of

number = 0
x = []

while True:
    s = input(f'x[{number}]값을 입력하세요.: ')

    if s == "End":
        break

    x.append(s)
    number += 1

print(f"총 입력 횟수는 {number}입니다.")
print(f'최댓값은 {max_of(x)}입니다.')