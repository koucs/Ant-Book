#! env python
# -*- coding: utf-8 -*-
import pprint
import sys

# Ant-Book.main.py
# Date: 2021/12/07
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
    m = list(map(int, input().split()))
    K = int(input())

    dp = [[False] * (K + 1) for _ in range(n + 1)]

    # Calculate order: O(K Σ(m[i]) => TLE
    dp[0][0] = True
    for i in range(n):
        for j in range(K + 1):
            k = 0
            while k <= m[i] and (k * a[i]) <= j:
                # |= : in-place OR operation
                # https://stackoverflow.com/questions/3929278/what-does-ior-do-in-python
                dp[i + 1][j] |= dp[i][j - (k * a[i])]
                k += 1

    pprint.pprint(dp)

    if dp[n][K]:
        print("Yes")
    else:
        print("No")
    return


if __name__ == '__main__':
    main()
