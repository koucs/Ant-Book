#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

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
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    st = []
    for i in range(n):
        st.append((s[i], t[i]))

    ans, t = 0, 0
    sorted(st, key=lambda ent: ent[1])

    for i in range(n):
        if t < st[i][0]:
            ans += 1
            t = st[i][1]

    print(ans)
    return


if __name__ == '__main__':
    main()
