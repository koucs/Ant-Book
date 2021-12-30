#! env python
# -*- coding: utf-8 -*-

import bisect
import sys

# Ant-Book.main.py
# Date: 2021/12/30
# Filename: main.py 
# Author: koucs

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]
input = sys.stdin.readline


def main():
    a = []
    bisect.insort_left(a, 1)
    bisect.insort_left(a, 3)
    bisect.insort_left(a, 5)
    for i, v in enumerate(a):
        print(f"{i}, {v}")

    index = bisect.bisect_left(a, 3)
    if index == -1:
        print("found")
    else:
        print("not found")

    del a[index]
    index = bisect.bisect_left(a, 3)
    if index == -1:
        print("found")
    else:
        print("not found")
    for i, v in enumerate(a):
        print(f"{i}, {v}")

    print("== insert ==")
    a.insert(index, 4)
    for i, v in enumerate(a):
        print(f"{i}, {v}")

    print("== insert ==")
    bisect.insort_left(a, 2)
    for i, v in enumerate(a):
        print(f"{i}, {v}")

    return


if __name__ == '__main__':
    main()
