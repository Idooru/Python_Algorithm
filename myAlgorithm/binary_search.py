from typing import Sequence, Any


def binary_search(arr: Sequence, target: Any) -> int:
    """이진검색 입니다."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        center = (low + high) // 2
        guess = arr[center]

        if guess == target:
            return center

        if guess < target:
            low = center + 1

        if guess > target:
            high = center - 1

    return -1


if __name__ == "__main__":
    num = int(input('배열 원소의 개수를 입력하세요.: '))
    x = [None] * num

    x[0] = int(input(f'x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] > x[i - 1]:
                break

    target = int(input('검색하려는 값을 입력하세요.: '))
    idx = binary_search(x, target)

    if idx == -1:
        print('찾으려는 값이 존재하지 않습니다.')
    else:
        print(f'검색하려는 값({target})이 x[{idx}]에 존재합니다.')
