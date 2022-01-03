#! env python
# -*- coding: utf-8 -*-

# Ant-Book.main.py
# Date: 2022/01/03
# Filename: main.py 
# Author: koucs


import sys

sys.path.insert(0, '../../utils')
from prime import is_prime


def mod_pow(x: int, n: int, modulo: int) -> int:
    res = 1
    while n > 0:
        if n & 1:
            res = res * x % modulo
        x = x * x % modulo
        n >>= 1
    return res


def main():
    n = int(input())

    if is_prime(n):  # 素数判定
        print("No")
        return

    # 任意の 1<x<n でループ
    for x in range(2, n):
        # pow(x, n, n) で代替可
        if mod_pow(x, n, n) != x:
            print("No")
            return

    print("Yes")
    return


if __name__ == '__main__':
    main()
