#! env python
# -*- coding: utf-8 -*-
import pprint
import sys

# Ant-Book.main.py
# Date: 2021/12/30
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
    V = int(input())  # vertex num
    N = int(input())  # edge num
    G = [[] for _ in range(V)]  # Graph
    for i in range(N):
        i, j = map(int, input().split())
        G[i].append(j)
        G[j].append(i)

    color = [0 for _ in range(V)]  # initialize as "0"

    def dfs(v: int, c: int) -> bool:
        color[v] = c
        for i in range(len(G[v])):
            if color[G[v][i]] == c:
                return False
            if color[G[v][i]] == 0 and not dfs(G[v][i], -c):
                return False
        return True

    for i in range(V):
        if color[i] == 0:
            if not dfs(i, 1):
                print("No")
                return

    print("Yes")
    return


if __name__ == '__main__':
    main()
