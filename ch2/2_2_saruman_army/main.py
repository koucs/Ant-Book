#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

# Ant-Book.main.py
# Date: 2021/08/29
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
    n = int(input())
    r = int(input())
    x = list(map(int, input().split()))
    x.sort()

    i, ans = 0, 0
    while i < n:
        # s: most left point
        s = x[i]
        while i < n and x[i] <= s + r:
            i += 1

        # p: marked point
        p = x[i-1]
        while i < n and x[i] <= p + r:
            i += 1

        ans += 1

    print(ans)
    return


if __name__ == '__main__':
    main()
