existArr = [5, 6, 14, 20, 29, 34, 35, 37, 51, 69, 75]
hashedArr = [None] * len(existArr)
hashKey = 13

print(f'기존 배열:\n{existArr}')

i = 0
while i < len(existArr):
    for j in existArr:
        hashedArr[i] = j % hashKey
        i += 1

print(f'해시값으로 만든 새로운 배열:\n{hashedArr}')

newArr = [None] * hashKey

i = 0
while i < len(existArr):
    for j in existArr:
        formula = j % hashKey
        newArr[formula] = existArr[i]
        i += 1

print(f'새로운 배열:\n{newArr}')
