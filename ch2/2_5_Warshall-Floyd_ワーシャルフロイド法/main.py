#! env python
# -*- coding: utf-8 -*-
import sys

# Ant-Book.main.py
# Date: 2022/01/01
# Filename: main.py 
# Author: koucs

INF = float('inf')
input = sys.stdin.readline


def main():
    V, E = map(int, input().split())
    L = []
    for i in range(V):
        l = []
        for j in range(V):
            if i == j:
                l.append(0)
            else:
                l.append(INF)
        L.append(l)

    for i in range(E):
        f, t, v = map(int, input().split())
        L[f][t] = v

    for k in range(V):
        for i in range(V):
            for j in range(V):
                L[i][j] = min(L[i][j], L[i][k] + L[k][j])

    print(L)
    return


if __name__ == '__main__':
    main()
