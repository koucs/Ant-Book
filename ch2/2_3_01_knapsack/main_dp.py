#! env python
# -*- coding: utf-8 -*-
import sys

# Ant-Book.main.py
# Date: 2021/08/28
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

    for i in range(N - 1, -1, -1):
        for j in range(W + 1):
            if j < w[i]:
                dp[i][j] = dp[i + 1][j]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i])

    print(dp[0][W])

    return


if __name__ == '__main__':
    main()
