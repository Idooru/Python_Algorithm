from typing import Sequence, Any
from copy import deepcopy


def linear_search(arr: Sequence, target: Any) -> int:
    """보초법을 사용한 선형검색입니다."""
    sentinel = deepcopy(arr)
    sentinel.append(target)
    i = 0

    while True:
        if sentinel[i] == target:
            break
        i += 1

    return -1 if i == len(arr) else i


if __name__ == "__main__":
    num = int(input('배열 원소의 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    target = int(input('검색하려는 값을 입력하세요.: '))
    result = linear_search(x, target)

    if result == -1:
        print('값을 찾는데 실패하였습니다.')
    else:
        print(f'{target}은 x[{result}]에 위치합니다.')
