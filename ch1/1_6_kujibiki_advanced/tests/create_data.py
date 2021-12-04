#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest
import random

# Ant-Book.main.py
# Date: 2021/08/05
# Filename: main.py
# Author: acttrd

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]
input = sys.stdin.readline


def main():

    l = list(range(100000))
    sample_l = random.sample(l, 1000)
    for i in sample_l:
        print(i, end=" ")

    sample_sample_l = random.sample(sample_l, 4)
    print()

    ans = 0
    for i in sample_sample_l:
        print(i, end=" ")
        ans += i
    print()
    print(ans)
    return


if __name__ == '__main__':
    main()
