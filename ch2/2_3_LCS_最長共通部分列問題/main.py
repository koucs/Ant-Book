#! env python
# -*- coding: utf-8 -*-
import pprint
import sys

# Ant-Book.main.py
# Date: 2021/08/28
# Filename: main.py 
# Author: acttrd

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]
input = sys.stdin.readline


def main():
    n = int(input())
    m = int(input())
    s = input()
    t = input()
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j], dp[i][j + 1])
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    pprint.pprint(dp)
    print(dp[n][m])

    return


if __name__ == '__main__':
    main()
