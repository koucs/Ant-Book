#! env python
# -*- coding: utf-8 -*-
import pprint
import sys

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


# 重複組み合わせ: https://phyllo-algo.hatenadiary.org/entry/20140831/1409502655
def main():
    n, m = int(input()), int(input())
    a = list(map(int, input().split()))
    M = int(input())

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1

    # Calculate Order: O(nm^2)
    for i in range(0, n):
        for j in range(1, m + 1):
            for k in range(min(j, a[i]) + 1):
                dp[i + 1][j] += dp[i][j - k]

    print(dp[n][m])
    return


if __name__ == '__main__':
    main()
