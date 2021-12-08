#! env python
# -*- coding: utf-8 -*-
import pprint
import sys
from bisect import bisect_left

# Ant-Book.main.py
# Date: 2021/12/08
# Filename: main.py 
# Author: koucs

sys.setrecursionlimit(10 ** 8)
INF = 10 ** 18
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]
input = sys.stdin.readline


def main():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [INF] * n

    pprint.pprint(dp)
    for i in range(n):
        dp[bisect_left(dp, a[i])] = a[i]

    print(bisect_left(dp, INF))
    return


if __name__ == '__main__':
    main()
