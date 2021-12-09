#! env python
# -*- coding: utf-8 -*-
import pprint
from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

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

# 書籍に載っている”間違っている解法"を実装したもの
def main():
    n, m, M = int(input()), int(input()), int(input())
    dp = [[0] * (n) for _ in range(m+1)]
    dp[1] = [1] * n

    for i in range(1, m):
        for j in range(n):
            for k in range(j):
                dp[i+1][j] += dp[i][j-k]

    pprint.pprint(dp)
    return


if __name__ == '__main__':
    main()
