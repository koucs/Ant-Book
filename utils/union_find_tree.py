#! env python
# -*- coding: utf-8 -*-
import datetime
import sys

# Ant-Book.union_find_tree.py
# Date: 2021/12/30
# Filename: union_find_tree.py
# Author: koucs

INF = float('inf')
par = list()  # parent of each element
rank = list()  # depth of each element


def init(n: int):
    # Python: Modify Global list inside a function
    # https://stackoverflow.com/questions/31435603/python-modify-global-list-inside-a-function
    rank[:] = [0 for i in range(n + 1)]
    par[:] = [i for i in range(n + 1)]


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
