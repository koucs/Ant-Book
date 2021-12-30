#! env python
# -*- coding: utf-8 -*-

import heapq
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
    N = int(input())
    L = list(map(int, input().split()))

    ans = 0
    que = list(L)
    heapq.heapify(que)

    for i in range(N - 1):
        # print(f"{i}, {que}, {ans}")
        total = heapq.heappop(que) + heapq.heappop(que)
        ans += total
        heapq.heappush(que, total)

    print(ans)
    return


if __name__ == '__main__':
    main()
