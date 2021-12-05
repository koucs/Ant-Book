#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

# Ant-Book.main.py
# Date: 2021/08/05
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
    m = int(input())
    k = list(map(int, input().split()))

    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if k[a] + k[b] + k[c] + k[d] == m:
                        print("Yes")
                        return
    print("No")
    return


if __name__ == '__main__':
    main()
