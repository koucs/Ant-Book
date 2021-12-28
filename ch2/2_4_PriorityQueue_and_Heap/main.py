#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

# Ant-Book.main.py
# Date: 2021/12/28
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
    l1 = [1, 2, 4, 7, 8, 5]
    heapq.heapify(l1)
    print(l1)

    heapq.heappush(l1, 3)
    print(l1)

    l2 = [1, 2, 4, 7, 8, 5]
    heapq.heapify(l2)
    print(l2)

    heapq.heappop(l2)
    print(l2)

    l2 = [1, 2, 4, 7, 8, 5]
    heapq.h(l2)
    print(l2)

    heapq.heappop(l2)
    print(l2)

    return


if __name__ == '__main__':
    main()
