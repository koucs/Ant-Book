#! env python
# -*- coding: utf-8 -*-
import pprint
import sys

# Ant-Book.main.py
# Date: 2021/12/08
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
    n = int(input())
    a = list(map(int, input().split()))

    dp = [0] * n
    ans = 0
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        ans = max(ans, dp[i])

    print(ans)
    return


if __name__ == '__main__':
    main()
