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

# 動的計画法における重複組み合わせの式変形について: https://emtubasa.hateblo.jp/entry/2018/08/29/161456
# 重複組合せ: https://www.ryoppei.com/%E3%80%90%E5%88%9D%E5%BF%83%E8%80%85%E3%81%8C%E3%80%91python%E3%81%A7%E8%9F%BB%E6%9C%AC%E3%82%92%E8%A7%A3%E3%81%84%E3%81%A6%E3%81%BF%E3%81%9F-part13/
def main():
    n, m = int(input()), int(input())
    a = list(map(int, input().split()))
    M = int(input())

    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1

    # Calculate Order: O(nm)
    for i in range(n):
        for j in range(1, m + 1):
            if (j - 1 - a[i]) >= 0:
                dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j] - dp[i][j - 1 - a[i]] + M) % M
            else:
                dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j]) % M
    print(dp[n][m])
    return


if __name__ == '__main__':
    main()
