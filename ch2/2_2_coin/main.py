#! env python
# -*- coding: utf-8 -*-

import sys

# Ant-Book.main.py
# Date: 2021/08/28
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
    v = [1, 5, 10, 50, 100, 500]
    c = list(map(int, input().split()))
    a = int(input())

    ans = 0
    for i in range(5, -1, -1):
        count_coin = min(a // v[i], c[i])
        ans += count_coin
        a -= v[i] * count_coin
    print(ans)
    return


if __name__ == '__main__':
    main()
