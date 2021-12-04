#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

# Ant-Book.main.py
# Date: 2021/08/01
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
    l = int(input())
    n = int(input())
    x = list(map(int, input().split()))

    min_val = 0
    for x_val in x:
        min_val = max(min_val, min(x_val, l - x_val))
    print(min_val)

    max_val = 0
    for x_val in x:
        max_val = max(max_val, max(x_val, l - x_val))
    print(max_val)

    return


if __name__ == '__main__':
    main()
