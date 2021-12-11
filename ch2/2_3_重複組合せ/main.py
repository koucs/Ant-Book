#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

# Ant-Book.main.py
# Date: 2021/12/11
# Filename: main.py 
# Author: koucs

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]
input = sys.stdin.readline

MAX_N = 1000
MAX_M = 10000


def main():
    n, m = int(input()), int(input())
    a = list(map(int, input().split()))
    M = int(input())

    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(n):
        for j in range(1, m+1):
            if (j - 1 -a[i]) >= 0:
                dp[i+1][j] = (dp[i+1][j-1] + dp[i][j] - dp[i][j - 1 - a[i]] + M) % M
            else:
                dp[i+1][j] = (dp[i+1][j-1] + dp[i][j]) % M

    print(dp[n][m])
    return


if __name__ == '__main__':
    main()
