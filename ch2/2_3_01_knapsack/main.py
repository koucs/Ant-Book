#! env python
# -*- coding: utf-8 -*-

import sys

# Ant-Book.main.py
# Date: 2021/08/28
# Filename: main.py 
# Author: acttrd
import pprint

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]
input = sys.stdin.readline


def main():
    N = int(input())
    w, v = list(), list()
    for i in range(N):
        i, j = map(int, input().split())
        w.append(i)
        v.append(j)
    W = int(input())
    dp = [[0] * (W+1) for _ in range(N+1)]

    def rec(depth, weight):

        if dp[depth][weight] != 0:
            return dp[depth][weight]

        res = int()
        if depth == N:
            res = 0
        elif weight < w[depth]:
            # cannot append to a knapsack
            res = rec(depth + 1, weight)
        else:
            res = max(rec(depth + 1, weight - w[depth]) + v[depth], rec(depth + 1, weight))
        dp[depth][weight] = res
        return res
    res = rec(0, W)
    print(res)

    return


if __name__ == '__main__':
    main()
