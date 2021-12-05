#! env python
# -*- coding: utf-8 -*-

import sys

# Ant-Book.main.py
# Date: 2021/08/29
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
    s = input()

    a, b = 0, n - 1
    t = ""
    while a <= b:
        left = False
        for i in range(b - a + 1):  # 0 <= i <= b - a
            if s[a + i] < s[b - i]:
                left = True
                break
            elif s[a + i] > s[b - i]:
                left = False
                break
        if left:
            t += s[a]
            a += 1
        else:
            t += s[b]
            b -= 1

    print(t)
    return


if __name__ == '__main__':
    main()
