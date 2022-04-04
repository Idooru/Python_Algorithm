from typing import Sequence, Any
import copy


def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1

    return -1 if i == len(seq) else i


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