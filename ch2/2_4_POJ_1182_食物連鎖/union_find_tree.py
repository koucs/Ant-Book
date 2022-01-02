#! env python
# -*- coding: utf-8 -*-
import time
from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

# Ant-Book.main.py
# Date: 2021/12/30
# Filename: unon_find_tree.py
# Author: koucs

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]
input = sys.stdin.readline

par = list()   # parent of each element
rank = list()  # depth of each element


def init(n: int):
    # Python: Modify Global list inside a function
    # https://stackoverflow.com/questions/31435603/python-modify-global-list-inside-a-function
    rank[:] = [0 for i in range(n+1)]
    par[:] = [i for i in range(n+1)]


def find(x: int) -> int:
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x: int, y: int):
    x = find(x)
    y = find(y)
    if x == y:
        return

    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


def same(x: int, y: int) -> bool:
    return find(x) == find(y)


def print_status(n: int):
    print(datetime.datetime.now())
    for i in range(n):
        print(f"{i}: par={par[i]}, rank={rank[i]}")


def main():
    init(7)

    unite(2, 5)
    unite(1, 2)
    print_status(7)

    unite(3, 4)
    unite(3, 6)
    unite(3, 7)
    print_status(7)

    print(same(4, 6))
    print(same(1, 3))

    # 2's rank ++
    unite(2, 3)
    print_status(7)
    return


if __name__ == '__main__':
    main()
