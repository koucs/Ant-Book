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
    N = int(input())
    L = list(map(int, input().split()))

    ans = 0

    while N > 1:
        mii1, mii2 = 0, 1
        if L[mii1] > L[mii2]:
            mii1, mii2 = mii2, mii1

        for i in range(2, N):
            if L[i] < L[mii1]:
                mii1, mii2 = i, mii1
            elif L[i] < L[mii2]:
                mii2 = i

        t = L[mii1] + L[mii2]
        ans += t

        if mii1 == N-1:
            mii1, mii2 = mii2, mii1

        L[mii1] = t
        L[mii2] = L[N-1]

        N-=1

    print(ans)

    return


if __name__ == '__main__':
    main()
