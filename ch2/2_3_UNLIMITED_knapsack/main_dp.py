#! env python
# -*- coding: utf-8 -*-
import pprint
import sys

# Ant-Book.main.py
# Date: 2021/12/05
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
    w, v = list(), list()
    for i in range(N):
        i, j = map(int, input().split())
        w.append(i)
        v.append(j)
    W = int(input())
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    # Calculate order: O(nW)
    for i in range(N):
        for j in range(W + 1):
            if j < w[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - w[i]] + v[i])

    print(dp[N][W])
    return


if __name__ == '__main__':
    main()
