#! env python
# -*- coding: utf-8 -*-
import sys

# Ant-Book.main.py
# Date: 2021/08/28
# Filename: main.py 
# Author: koucs

sys.setrecursionlimit(10 ** 8)
INF = 1_000
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
    MAX_W, MAX_V = max(w), max(v)
    dp = [[0] * (MAX_W * MAX_V + 1) for _ in range(N + 1)]
    for i in range(MAX_W * MAX_V):
        dp[0][i + 1] = int(INF)

    for i in range(N):
        for j in range(MAX_W * MAX_V + 1):
            if j < v[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = min(dp[i][j], dp[i][j - v[i]] + w[i])

    ans = 0
    for i in range(MAX_W * MAX_V + 1):
        if dp[N][i] <= W:
            ans = i
    print(ans)
    return


if __name__ == '__main__':
    main()
