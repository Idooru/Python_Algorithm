from ctypes.wintypes import PINT
from typing import Any, MutableSequence


def reverse_array(a: MutableSequence) -> Any:
    """뮤터블 시퀀스 a의 원소를 역순으로 정렬"""
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]


if __name__ == "__main__":
    print("배열 원소를 역순으로 정렬합니다.")
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]값을 입력하세요.: "))

    reverse_array(x)  # x를 역순으로 정렬

    print("배열 원소를 역순으로 정렬했습니다.")
    for i in range(num):
        print(f'x[{i}] = {x[i]}')