from telnetlib import SE
from typing import Sequence, Any


def seq_search(a: Sequence, key: Any) -> int:
    n = len(a)
    for i in range(n):
        if a[i] == key:
            return i
    return -1


if __name__ == "__main__":
    num = int(input('배열 원소의 개수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    target = int(input('검색하려는 값을 입력하세요.: '))
    idx = seq_search(x, target)

    if idx == -1:
        print(False)

    else:
        print(f'검색하려는 값({target})은 x[{idx}]에 존재합니다.')