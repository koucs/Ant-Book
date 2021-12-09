#! env python
# -*- coding: utf-8 -*-
import pprint
import sys

# Ant-Book.main.py
# Date: 2021/12/09
# Filename: main.py 
# Author: koucs

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]
input = sys.stdin.readline

MAX_N = MAX_M = 1000


# "分割数"の理解の参考になった解説
# https://scrapbox.io/pocala-kyopro/%E5%88%86%E5%89%B2%E6%95%B0
def main():
    n, m, M = int(input()), int(input()), int(input())
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = 1
    for i in range(1, m + 1):  # no need to consider "0" divide
        for j in range(n + 1):
            if (j - i) < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - i] + dp[i - 1][j]

    pprint.pprint(dp)
    print(dp[m][n])
    return


if __name__ == '__main__':
    main()
