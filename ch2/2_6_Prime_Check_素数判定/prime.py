#! env python
# -*- coding: utf-8 -*-

# Ant-Book.prime.py
# Date: 2022/01/02
# Filename: prime.py
# Author: koucs
from typing import List, Dict


def divisor(n: int) -> List[int]:
    i = 1
    res = []
    while i * i <= n:
        if n % i == 0:
            res.append(i)
            if i != (n // i):
                res.append(n // i)
        i += 1
    return res


def prime_factor(n: int) -> Dict[int, int]:
    i = 2
    res = {}
    while i * i <= n:
        while n % i == 0:
            if i not in res:
                res[i] = 0
            res[i] += 1
            n //= i
        i += 1
    if n != 1:
        res[n] = 1
    return res


def main():
    n = int(input())
    ans1 = divisor(n)
    print(*ans1)
    ans2 = prime_factor(n)
    print(ans2)
    return


if __name__ == '__main__':
    main()
