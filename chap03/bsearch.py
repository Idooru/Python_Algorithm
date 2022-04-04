from typing import Sequence, Any


def binary_search(a: Sequence, key: Any) -> int:
    low = 0
    high = len(a) - 1

    while True:
        mid = (low + high) // 2
        guess = a[mid]

        if guess == key:
            return mid

        if guess < key:
            low = mid + 1

        if guess > key:
            high = mid - 1

        if low > high:
            break

    return -1


if __name__ == "__main__":
    num = int(input('배열 원소의 개수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    target = int(input('검색하려는 값을 입력하세요.: '))
    idx = binary_search(x, target)

    if idx == -1:
        print(False)

    else:
        print(f'검색하려는 값({target})은 x[{idx}]에 존재합니다.')