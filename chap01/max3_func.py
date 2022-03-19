def max3(a, b, c):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum


paramList = [
    [3, 2, 1],
    [
        3,
        2,
        2,
    ],
    [3, 1, 2],
    [3, 2, 3],
    [2, 1, 3],
    [3, 3, 2],
    [
        3,
        3,
        3,
    ],
    [2, 2, 3],
    [2, 3, 1],
    [2, 3, 2],
    [
        1,
        3,
        2,
    ],
    [
        2,
        3,
        3,
    ],
    [
        1,
        2,
        3,
    ],
]

for i in range(len(paramList)):
    result = max3(paramList[i][0], paramList[i][1], paramList[i][2])
    print(f"max3{paramList[i][0], paramList[i][1], paramList[i][2]} = ", result)
