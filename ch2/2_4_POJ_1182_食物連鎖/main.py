#! env python
# -*- coding: utf-8 -*-

import sys

from unon_find_tree import init, same, unite, find, print_status

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
    N, K = map(int, input().split())
    TYPES, X, Y = list(), list(), list()
    for i in range(K):
        i, j, k = map(int, input().split())
        TYPES.append(i)
        X.append(j)
        Y.append(k)

    init(N * 3)
    ans = 0

    for i in range(K):
        t, x, y = TYPES[i], X[i] - 1, Y[i] - 1
        if x < 0 or N <= x or y < 0 or N <= y:
            # print(f"i: {i}, t: {t}, x: {x}, y: {y}")
            ans += 1
            continue

        if t == 1:
            if same(x, y + N) or same(x, y + 2 * N):
                # print(f"i: {i}, t: {t}, x: {x}, y: {y}, "
                #       f"same(x, y + N): {same(x, y + N)}, same(x, y + 2 * N): {same(x, y + 2 * N)}")
                ans += 1
            else:
                unite(x, y)
                unite(x + N, y + N)
                unite(x + 2 * N, y + 2 * N)
        else:
            # もし type=2 で同じ種類の動物を指定された場合は same(x, y) == True となり矛盾する
            #
            if same(x, y) or same(x, y + 2 * N):
                # print(f"i: {i}, t: {t}, x: {x}, y: {y}, "
                #       f"same(x, y): {same(x, y)}, same(x, y + 2 * N): {same(x, y + 2 * N)}")
                ans += 1
            else:
                unite(x, y + N)
                unite(x + N, y + 2 * N)
                unite(x + 2 * N, y)

    # test-1.in 実行時の print_statusの結果 (一部抜粋)
    # 0: par=0, rank=1
    # 1: par=200, rank=0
    # 2: par=100, rank=0
    # ...
    # 100: par=100, rank=1
    # 101: par=0, rank=0
    # 102: par=200, rank=0
    # ...
    # 200: par=200, rank=1
    # 201: par=100, rank=0
    # 202: par=0, rank=0
    # print_status(N*3)
    print(ans)
    return


if __name__ == '__main__':
    main()
