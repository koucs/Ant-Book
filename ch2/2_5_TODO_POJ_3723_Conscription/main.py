#! env python
# -*- coding: utf-8 -*-

import sys

from prim import prim

# Ant-Book.main.py
# Date: 2022/01/01
# Filename: main.py 
# Author: koucs

INF = float('inf')


def main():
    N, M, R = map(int, input().split())
    cost = [[INF] * (N+M) for _ in range(N+M)]
    for i in range(R):
        x, y, d = map(int, input().split())
        cost[x][y + N] = -d
        cost[y + M][x] = -d

    # TODO:
    #  Need to Modify
    #  cost[4][4] will contain "inf" and it will mislead the incorrect answer.
    print(prim(N + M, R, cost))
    return


if __name__ == '__main__':
    main()
