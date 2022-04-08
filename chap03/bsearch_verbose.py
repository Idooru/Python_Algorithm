from telnetlib import SE
from typing import Sequence, Any

def binary_search(a: Sequence, key: Any) -> int:
    '''시퀀스 a에서 key와 일치하는 원소를 이진 검색(실행 과정을 출력)'''
    low = 0
    high = len(a) - 1
    
    print('   |', end='')
    for i in range(len(a)):
        print(f'{i : 4}', end='')
    print()
    print('---+' + (4 * len(a) + 2) * '-')
    
    while True:
        mid = (low + high) // 2

        print('   |', end='')
        if low != mid:
            print((low * 4 + 1) * ' ' + '<-' + ((mid - low) * 4) * ' ' + '+', end='')
        else:
            print((mid * 4 + 1) * ' ' + '<+', end='')
        if mid != high:
            print(((high - mid) * 4 - 2) * ' ' + '->')       
        else:
            print('->')
        print(f'{mid : 3}|', end='')
        for i in range(len(a)):
            print(f'{a[i] : 4}', end='')
        print('\n   |')
        
        if a[mid] == key:
            return mid

        if a[mid] < key:
            low = mid + 1

        if a[mid] > key:
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