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

    dp = [[-1] * (K + 1) for _ in range(n + 1)]

    # Calculate order: O(nK) => AC
    dp[0][0] = 0
    for i in range(n):
        for j in range(K + 1):
            if dp[i][j] >= 0:
                dp[i + 1][j] = m[i]
            elif j < a[i] or dp[i + 1][j - a[i]] <= 0:
                dp[i + 1][j] = -1
            else:
                dp[i + 1][j] = dp[i + 1][j - a[i]] - 1

    pprint.pprint(dp)

    if dp[n][K] >= 0:
        print("Yes")
    else:
        print("No")
    return


if __name__ == '__main__':
    main()
